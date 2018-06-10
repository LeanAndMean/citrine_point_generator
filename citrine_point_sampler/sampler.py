#!/usr/bin/env python
"""Generates points in high dimensional space subject to a set of constraints."""

import sys
import citrine_point_sampler
import numpy as np


__author__ = "Kevin Ryan"
__created__ = "6/9/2018"

def main():
  args = citrine_point_sampler.console.parse_args(sys.argv[1:])
  # Parse constraints input file.
  constraints = citrine_point_sampler.constraint_parser.Constraint(
    args.input_file)
  # Generate points.
  points = citrine_point_sampler.generator.rejection_sampling.generate_points(
    args.n_results,
    constraints)
  # Write to disk.
  np.savetxt(args.output_file,points,delimiter=' ')
  


if __name__ == "__main__":
  main()