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
  parser.add_argument(
    'output_file',
    type=argparse.FileType('w'),
    help='Filepath for output file that will be generated.')
  parser.add_argument(
    'n_results',
    type=check_positive,
    help='Number of points to generate.')
  return parser.parse_args(args)