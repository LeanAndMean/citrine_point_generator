"""Tests rejection sampling generator."""

import os, pytest
import citrine_point_sampler

__author__ = "Kevin Ryan"
__created__ = "6/9/2018"

def get_points(example_input_file,n_points=1000):
  # Collect example failures and report after testing all of them.
  assert os.path.isfile(example_input_file)
  constraints = citrine_point_sampler.constraint_parser.Constraint(
    example_input_file)
  # Generate points.
  generated_points = citrine_point_sampler.generator.rejection_sampling.generate_points(
    n_points,
    constraints)
  # Print returned numpy array.
  print(generated_points)

# Using individual tests to avoid obscuring problem input files that timeout.
# alloy.txt is expected to timeout with rejection sampling.
@pytest.mark.timeout(300)
def test_alloy():
  get_points('.\\citrine_point_sampler\\tests\\Examples\\alloy.txt')

@pytest.mark.timeout(300)
def test_example():
  get_points('.\\citrine_point_sampler\\tests\\Examples\\example.txt')

@pytest.mark.timeout(300)
def test_formulation():
  get_points('.\\citrine_point_sampler\\tests\\Examples\\formulation.txt')

@pytest.mark.timeout(300)
def test_mixture():
  get_points('.\\citrine_point_sampler\\tests\\Examples\\mixture.txt')
