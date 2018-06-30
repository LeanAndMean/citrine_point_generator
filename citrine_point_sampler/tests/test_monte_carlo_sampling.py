"""Tests monte carlo sampling generator."""

import os, pytest, sys
import numpy as np
import citrine_point_sampler

__author__ = "Kevin Ryan"
__created__ = "6/30/2018"

@pytest.mark.parametrize(
  'point',
  [
    pytest.param([0.0,0.0,0.0]),
    pytest.param([0.0]),
    pytest.param([0.894534576]),
    pytest.param([0.0,0.1,0.0]),
    pytest.param([0.0,0.9]),
    pytest.param([0.0,0.3,0.0,0.7]),
    pytest.param([1.0,1.0,1.0]),
    pytest.param(
      [0.0,0.0,-0.5,0.0],
      marks=[pytest.mark.xfail(strict=True)]),
    pytest.param(
      [0.0,-1.0,-0.5],
      marks=[pytest.mark.xfail(strict=True)]),
    pytest.param(
      [0.1,-1.0,0.0],
      marks=[pytest.mark.xfail(strict=True)]),
    pytest.param(
      [0.1,0.0,5.0],
      marks=[pytest.mark.xfail(strict=True)])
  ])
def test_in_hypercube(point):
  assert citrine_point_sampler.generator.monte_carlo.in_hypercube(point)

@pytest.mark.parametrize(
  'point',
  [
    pytest.param([0.0,0.0,0.0]),
    pytest.param([0.0]),
    pytest.param([0.894534576]),
    pytest.param([0.0,0.1,0.0]),
    pytest.param([0.0,0.9]),
    pytest.param([0.0,0.3,0.0,0.7])
  ])
def test_generate_point(point):
  # Test behavior when offset is zero.
  modified_point = citrine_point_sampler.generator.monte_carlo.generate_point(
    point,
    0.0)
  print(modified_point)
  assert citrine_point_sampler.generator.monte_carlo.in_hypercube(modified_point)
  # Check if points were moved (no movement should occur when offset is 0).
  assert np.all((point-modified_point) < 1.e-12)
  # Test behavior when offset is too small to move point outside unit hypercube.
  modified_point = citrine_point_sampler.generator.monte_carlo.generate_point(
    point,
    0.05)
  print(modified_point)
  assert citrine_point_sampler.generator.monte_carlo.in_hypercube(modified_point)
  # Test behavior when offset is large enough to move point outside unit
  # hypercube. np.remainder(point,1.0) is expected to ensure that the value
  # is 
  modified_point = citrine_point_sampler.generator.monte_carlo.generate_point(
    point,
    5.0)
  print(modified_point)
  assert citrine_point_sampler.generator.monte_carlo.in_hypercube(modified_point)

def get_points(example_input_file,n_points=1000,timeout=20):
  # Collect example failures and report after testing all of them.
  assert os.path.isfile(example_input_file)
  constraints = citrine_point_sampler.constraint_parser.Constraint(
    example_input_file)
  if not citrine_point_sampler.generator.monte_carlo.in_hypercube(
      constraints.get_example()):
    msg = "Example point {} is not in hypercube.".format(constraints.get_example())
    raise RuntimeError(msg)
  # Generate points.
  generated_points = citrine_point_sampler.generator.monte_carlo.generate_points(
    n_points,
    constraints,
    timeout=timeout)
  # Print returned numpy array.
  print(generated_points)

# Using individual tests to avoid obscuring problem input files that timeout.
# alloy.txt is expected to timeout with rejection sampling.
@pytest.mark.timeout(300)
def test_alloy():
  # Print function name to identify problem input files.
  print("Running monte carlo test function:",sys._getframe().f_code.co_name)
  get_points('.\\citrine_point_sampler\\tests\\Examples\\alloy.txt')

@pytest.mark.timeout(300)
def test_example():
  print("Running monte carlo test function:",sys._getframe().f_code.co_name)
  get_points('.\\citrine_point_sampler\\tests\\Examples\\example.txt')

@pytest.mark.timeout(300)
def test_formulation():
  print("Running monte carlo test function:",sys._getframe().f_code.co_name)
  get_points('.\\citrine_point_sampler\\tests\\Examples\\formulation.txt')

@pytest.mark.timeout(300)
def test_mixture():
  print("Running monte carlo test function:",sys._getframe().f_code.co_name)
  get_points('.\\citrine_point_sampler\\tests\\Examples\\mixture.txt')
