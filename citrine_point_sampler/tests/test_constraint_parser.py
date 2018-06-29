"""Tests the constraint parser."""

import os, pytest
import citrine_point_sampler

__author__ = "Kevin Ryan"
__created__ = "6/9/2018"

# strict=True makes pytest treat unexpected successes as failures.
@pytest.mark.parametrize('example_input_file',
  [
    pytest.param('.\\citrine_point_sampler\\tests\\Examples\\alloy.txt'),
    pytest.param(
      '.\\citrine_point_sampler\\tests\\Examples\\alloy_bad.txt',
      marks=[pytest.mark.xfail(strict=True)]),
    pytest.param('.\\citrine_point_sampler\\tests\\Examples\\example.txt'),
    pytest.param('.\\citrine_point_sampler\\tests\\Examples\\formulation.txt'),
    pytest.param(
      '.\\citrine_point_sampler\\tests\\Examples\\formulation_bad.txt',
      marks=[pytest.mark.xfail(strict=True)]),
    pytest.param('.\\citrine_point_sampler\\tests\\Examples\\mixture.txt')
  ])
def test_constraint_parser(example_input_file):
  assert os.path.isfile(example_input_file)
  constraints = citrine_point_sampler.constraint_parser.Constraint(example_input_file)
  assert isinstance(constraints.get_example(),list)
  assert isinstance(constraints.get_ndim(),int)
  assert constraints.apply(constraints.get_example())