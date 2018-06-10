"""Tests the constraint parser."""

import os, pytest, sys
import citrine_point_sampler

__author__ = "Kevin Ryan"
__created__ = "6/9/2018"

def test_constraint_parser(example_input_files):
  example_failures = []
  for example_filepath in example_input_files:
    try:
      constraints = citrine_point_sampler.constraint_parser.Constraint(example_filepath)
      assert isinstance(constraints.get_example(),list)
      assert isinstance(constraints.get_ndim(),int)
    except:
      example_failures.append([example_filepath,str(sys.exc_info()[1])])
  if len(example_failures) > 0:
    print("{:d} failing example(s):".format(len(example_failures)))
    for failures in example_failures:
      print(' - '.join(failures))
  assert len(example_failures) == 0
