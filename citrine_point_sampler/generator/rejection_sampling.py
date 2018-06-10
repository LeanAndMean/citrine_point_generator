"""Performs rejection sampling to generate points that satisfy a set of constraints."""

import numpy as np

__author__ = "Kevin Ryan"
__created__ = "6/9/2018"

def generate_point(n_dim):
  return np.random.rand(n_dim)

def generate_valid_point(constraints):
  proposed_point = generate_point(constraints.n_dim)
  while not constraints.apply(proposed_point):
    proposed_point = generate_point(constraints.n_dim)
  # SanityCheck: Generated point is considered valid (by the set of constraints)
  assert constraints.apply(proposed_point)
  return proposed_point

def generate_points(n_results,constraints):
  results = np.ndarray([n_results,constraints.n_dim],dtype=np.float)
  for result_idx in range(n_results):
    valid_point = generate_valid_point(constraints)
    results[result_idx] = valid_point
  return results