"""Performs rejection sampling to generate points that satisfy a set of constraints."""

import time
import numpy as np

__author__ = "Kevin Ryan"
__created__ = "6/9/2018"

def generate_point(n_dim):
  return np.random.rand(n_dim)

def generate_valid_point(constraints,timeout,starttime):
  """ Generate a single valid point using rejection sampling.
  constraints: an instance of Constraint for testing generated points.
  timeout: maximum time in seconds that this function is allowed to run.
  starttime: starting time of function.
  """
  proposed_point = generate_point(constraints.n_dim)
  points_generated = 1
  while not constraints.apply(proposed_point):
    # Reduce performance impact of repeatedly calling time.time() by testing
    # every 100,000 steps.
    if points_generated % 100000 == 0 and time.time() - starttime > timeout:
      raise RuntimeError("Point generation exceeded timeout duration before completion.")
    proposed_point = generate_point(constraints.n_dim)
    points_generated += 1
  # SanityCheck: Generated point is considered valid (by the set of constraints)
  assert constraints.apply(proposed_point)
  return proposed_point

def generate_points(n_results,constraints,timeout=300):
  """ Generate points in a hypercube defined by constraints.
  n_results: number of points generated.
  constraints: an instance of Constraint for testing generated points.
  timeout: maximum time in seconds that this function is allowed to run.
  """
  results = np.ndarray([n_results,constraints.n_dim],dtype=np.float)
  # Start time.
  start = time.time()
  for result_idx in range(n_results):
    valid_point = generate_valid_point(constraints,timeout,start)
    results[result_idx] = valid_point
  return results