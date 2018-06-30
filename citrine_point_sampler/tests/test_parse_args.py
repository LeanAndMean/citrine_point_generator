"""Tests for the sampler argument parsing."""

import os, pytest, glob, tempfile
import citrine_point_sampler

__author__ = "Kevin Ryan"
__created__ = "6/9/2018"

@pytest.mark.parametrize('example_input_file',
  [
    pytest.param('.\\citrine_point_sampler\\tests\\Examples\\alloy.txt'),
    pytest.param('.\\citrine_point_sampler\\tests\\Examples\\example.txt'),
    pytest.param('.\\citrine_point_sampler\\tests\\Examples\\formulation.txt'),
    pytest.param('.\\citrine_point_sampler\\tests\\Examples\\mixture.txt')
  ])
@pytest.mark.parametrize('n_results',
  [
    pytest.param(1),
    pytest.param(10),
    pytest.param(
      0,
      marks=[pytest.mark.xfail(strict=True)]),
    pytest.param(
      -2,
      marks=[pytest.mark.xfail(strict=True)])
  ])
@pytest.mark.parametrize('timeout',
  [
    pytest.param(None),
    pytest.param(1),
    pytest.param(10),
    pytest.param(
      0,
      marks=[pytest.mark.xfail(strict=True)]),
    pytest.param(
      -2,
      marks=[pytest.mark.xfail(strict=True)])
  ])
def test_arg_parser(example_input_file,n_results,timeout):
  # Test if example files are found.
  temp_output_filename = tempfile.mktemp()
  assert os.path.isfile(example_input_file)
  assert not os.path.isfile(temp_output_filename)
  input_args = [
      example_input_file,
      temp_output_filename,
      str(n_results)
    ]
  if timeout is not None:
    input_args.extend(["--timeout",str(timeout)])
    assert len(input_args) == 5
  args = citrine_point_sampler.console.parse_args(input_args)
  assert args.input_file == example_input_file
  assert args.output_file == temp_output_filename
  assert args.n_results == n_results
  if timeout is None:
    assert args.timeout == 280
  else:
    assert args.timeout == timeout
    