"""Tests for the sampler argument parsing."""

import os, pytest, glob, tempfile
import citrine_point_sampler

__author__ = "Kevin Ryan"
__created__ = "6/9/2018"

def test_arg_parser(example_input_files):
  # Test if example files are found.
  temp_output_filename = tempfile.mktemp()
  for idx, filepath in enumerate(example_input_files):
    assert os.path.isfile(filepath)
    assert not os.path.isfile(temp_output_filename)
    args = citrine_point_sampler.console.parse_args(
      [
        filepath,
        temp_output_filename,
        str(idx+1)
      ])
    assert args.input_file == filepath
    assert args.output_file == temp_output_filename
    assert args.n_results == idx+1
