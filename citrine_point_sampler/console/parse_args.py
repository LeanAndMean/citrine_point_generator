"""Functions for parsing arguments from CLI."""
import argparse
from .argtypes import *
__author__ = "Kevin Ryan"
__created__ = "6/9/2018"


def parse_args(args):
  parser = argparse.ArgumentParser()
  parser.add_argument(
    'input_file',
    type=check_fname_exists,
    help='Path to file containing instructions for generating points.')
  # TODO - KR - Add safety checks for output file.
  # E.g., output file should not be the same as input file.
  parser.add_argument(
    'output_file',
    type=str,
    help='Filepath for output file that will be generated.')
  parser.add_argument(
    'n_results',
    type=check_positive,
    help='Number of points to generate.')
  parser.add_argument(
    '--timeout',
    type=check_positive,
    default=280,
    help='Seconds until script exists.')
  return parser.parse_args(args)