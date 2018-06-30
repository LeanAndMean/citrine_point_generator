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
  # Set timeout expectations for different generators.
  # TODO - KR - Switch to using a timer to get a more accurate measure of 
  # elapsed time.
  print(args.timeout)
  sys.stdout.flush()
  rejection_sampling_timeout = 20
  script_timeout = 280
  # Generate points.
  try:
    # Prioritize sampling uniformity: Try rejection sampling strategy first.
    points = citrine_point_sampler.generator.rejection_sampling.generate_points(
      args.n_results,
      constraints,timeout=rejection_sampling_timeout)
  except RuntimeError:
    # If rejection sampling times out, fallback to monte carlo sampling.
    points = citrine_point_sampler.generator.monte_carlo.generate_points(
      args.n_results,
      constraints,timeout = (script_timeout-rejection_sampling_timeout))
  # Write to disk.
  np.savetxt(args.output_file,points,delimiter=' ')

if __name__ == "__main__":
  main()