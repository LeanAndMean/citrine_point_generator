"""Tests rejection sampling generator."""

import os, pytest, glob, sys
import citrine_point_sampler

__author__ = "Kevin Ryan"
__created__ = "6/9/2018"

def test_rejection_sampling(example_input_files):
  # Collect example failures and report after testing all of them.
  example_failures = []
  for example_filepath in example_input_files:
    try:
      constraints = citrine_point_sampler.constraint_parser.Constraint(example_filepath)
      try:
        # Generate 10,000 points.
        generated_points = citrine_point_sampler.generator.rejection_sampling.generate_points(
          10000,
          constraints)
        # Print returned numpy array.
        print(generated_points)
      except:
        example_failures.append([example_filepath,str(sys.exc_info()[1])])
    except:
      # Disregard failures of parser (this is covered by a different unit test).
      pass
  if len(example_failures) > 0:
    print("{:d} failing example(s):".format(len(example_failures)))
    for failures in example_failures:
      print(' - '.join(failures))
  assert len(example_failures) == 0

