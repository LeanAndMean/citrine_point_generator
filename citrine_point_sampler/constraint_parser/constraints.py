"""Contains class for parsing and housing point generation constraints."""
import re

class Constraint():
  """Constraints loaded from a file."""

  def __init__(self, fname):
    """
    Construct a Constraint object from a constraints file

    :param fname: Name of the file to read the Constraint from (string)
    """
    with open(fname, "r") as f:
      lines = f.readlines()
    # Parse the dimension from the first line
    self.n_dim = int(lines[0])
    if self.n_dim <= 0:
      raise IOError("n_dim (number of dimensions) cannot be less than 1.")
    # Parse the example from the second line
    # Handle possibility of consecutive delimiters and trip trailing newline.
    self.example = [float(x) for x in re.split('[ ,]+',lines[1].strip('\n'))]
    if len(self.example) != self.n_dim:
      raise IOError("example dimensions are not equal to n_dim.")

    # Run through the rest of the lines and compile the constraints
    self.exprs = []
    for i in range(2, len(lines)):
      # support comments in the first line
      if lines[i][0] == "#":
        continue
      constraint = lines[i].strip('\n')
      self.exprs.append(compile(constraint, "<string>", "eval"))
    # SanityCheck: Example point should satisfy constraints.
    if not self.apply(self.get_example()):
      # Construct verbose error message.
      msg = "Example point does not satisfy the given constraints"
      msg += "\nPoint:\n  "
      msg += str(self.get_example())
      msg += "\nConstraints:\n"
      for i in range(2, len(lines)):
        # support comments in the first line
        if lines[i][0] == "#":
          continue
        constraint = lines[i].strip('\n')
        msg += "  "
        msg += str(constraint)
        msg += "\n"
      raise IOError(msg)
    return

  def get_example(self):
    """Get the example feasible vector"""
    return self.example

  def get_ndim(self):
    """Get the dimension of the space on which the constraints are defined"""
    return self.n_dim

  def apply(self, x):
    """
    Apply the constraints to a vector, returning True only if all are satisfied

    :param x: list or array on which to evaluate the constraints
    """
    for idx, expr in enumerate(self.exprs):
      if not eval(expr):
        return False
    return True
