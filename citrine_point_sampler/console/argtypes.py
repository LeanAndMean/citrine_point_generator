"""Functions for type-checking arguments."""
import os
import argparse
__author__ = "Kevin Ryan"
__created__ = "6/9/2018"

def check_positive(int_string):
  """Input Validation: int_string must cast to a positive integer."""
  value = int(int_string)
  if value <= 0:
    msg = "%r is not a positive integer." % value
    raise argparse.ArgumentTypeError(msg)
  return value

def check_fname_exists(input_file):
  """Input Validation: input_file must be a file that exists."""
  if not os.path.isfile(input_file):
    msg = "%r is not a file that exists." % input_file
    raise argparse.ArgumentTypeError(msg)
  return input_file
