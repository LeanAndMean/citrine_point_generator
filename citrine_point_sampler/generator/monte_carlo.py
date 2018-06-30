"""Generates points that satisfy a set of constraints by proposing modifications
 to a known example point.
"""

import time
import numpy as np

__author__ = "Kevin Ryan"
__created__ = "6/30/2018"

def in_hypercube(point,epsilon=1.e-12):
  """Tests if point is inside unit hypercube."""
  point = np.asarray(point)
  return np.all(point >= 0.0-epsilon) and np.all(point < 1.0+epsilon)

def generate_point(example_point,offset_factor):
  example_point = np.asarray(example_point)
  # Scale offset
  n_dim = example_point.size
  modification_index = np.random.randint(low=0,high=n_dim)
  assert isinstance(modification_index,int)
  assert modification_index < n_dim
  offset = (np.random.rand() - 0.5) * offset_factor
  assert isinstance(offset,float)
  proposed_point = example_point.copy()
  # Offset point using periodic boundary conditions to handle offsets outside
  # [0,1) interval.
  proposed_point[modification_index] = np.remainder(
    proposed_point[modification_index] + offset,
    1.0)
  return proposed_point

def draw_random_example(example_points):
  """Picks a random example from along the 0-axis of example_points.
  Returns a tuple containing the example point and index.
  """
  max_example_idx = example_points.shape[0]
  example_idx = np.random.randint(0,max_example_idx)
  return example_points[example_idx].copy(), example_idx

def generate_valid_point(example_points,constraints,timeout,starttime,offset_decay=0.999,return_example_index=False):
  """ Generate a single valid point by modifying an known example.
  example_point: point known to satisfy constraints.
  constraints: an instance of Constraint for testing generated points.
  timeout: maximum time in seconds that this function is allowed to run.
  starttime: starting time of function.
  offset_decay: controls how quickly the offset magnitude is reduced after each
  rejected modification.
  return_example_index: if True, also return index of example point used in the
  generation of the modified point.
  """
  example_point, example_idx = draw_random_example(example_points)
  if not constraints.apply(example_point):
    msg = "Example point {} does not satisfy constraints.".format((example_point))
    raise RuntimeError(msg)
  if not in_hypercube(example_point):
    msg = "Example point {} is not in hypercube.".format((example_point))
    raise RuntimeError(msg)
  # Offset factor makes this algorithm adaptive to the constraint difficulty.
  # This value is used to reduce the magnitude of the proposed offset each time
  # one is rejected.
  offset_factor = 1.0
  proposed_point = generate_point(example_point,offset_factor)
  assert constraints.apply(example_point)
  points_generated = 1
  while not constraints.apply(proposed_point):
    # Reduce performance impact of repeatedly calling time.time() by testing
    # every 100,000 steps.
    if points_generated % 100000 == 0 and time.time() - starttime > timeout:
      raise RuntimeError(
        "Point generation exceeded timeout duration before completion.")
    # Generate new point.
    example_point, example_idx = draw_random_example(example_points)
    offset_factor *= offset_decay
    proposed_point = generate_point(example_point,offset_factor)
    points_generated += 1
  # SanityCheck: Generated point is considered valid (by the set of constraints)
  assert constraints.apply(proposed_point)
  assert in_hypercube(proposed_point)
  if return_example_index:
    return (proposed_point, example_idx)
  else:
    return proposed_point

def generate_points(n_results,constraints,timeout=300):
  """ Generate points in a hypercube defined by constraints using MCMC.
  n_results: number of points generated.
  constraints: an instance of Constraint for testing generated points.
  timeout: maximum time in seconds that this function is allowed to run.
  """
  assert n_results > 0
  assert timeout > 0
  # Cache np.array copy of example point.
  constraint_example_point = np.asarray(constraints.get_example())
  if not in_hypercube(constraint_example_point):
    raise RuntimeError("Example point from Constraint class not in hypercube.")
  results = np.ndarray([n_results,constraints.n_dim],dtype=np.float)
  results[0] = constraint_example_point
  generated_points = 1
  # Start time.
  start = time.time()
  # Exit the loop 2 seconds before the timeout duration to avoid going over time.
  while time.time() - start < timeout - 2:
    # Fill results list.
    if generated_points < results.shape[0]:
      valid_point = generate_valid_point(
        results[:generated_points],
        constraints,
        timeout,
        start)
      results[generated_points] = valid_point
    else:
      # Perform random walk using examples in results. This is meant to
      # improve the quality of the results.
      valid_point, example_idx = generate_valid_point(
        results,
        constraints,
        timeout,
        start,
        return_example_index=True)
      results[example_idx] = valid_point
    generated_points += 1
  if generated_points < n_results:
    msg = "Failed to generate {} points before timeout.".format(n_results)
    raise RuntimeError(msg)
  return results