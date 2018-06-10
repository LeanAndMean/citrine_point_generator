"""Locates example input files."""

import os, pytest, sys
import glob

__author__ = "Kevin Ryan"
__created__ = "6/10/2018"

@pytest.fixture(scope="module")
def example_input_files():
  """Locates input file examples."""
  example_filepaths = [
    filepath for filepath in glob.glob('./**/tests/Examples/*.txt',recursive=True)]
  assert len(example_filepaths) > 0
  return example_filepaths

