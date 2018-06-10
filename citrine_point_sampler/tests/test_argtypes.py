"""Tests for the type checking functions in argtypes."""

import shutil, tempfile, os, unittest, argparse, glob
from citrine_point_sampler.console.argtypes import check_positive
from citrine_point_sampler.console.argtypes import check_fname_exists

__author__ = "Kevin Ryan"
__created__ = "6/9/2018"

class TestTypeChecking(unittest.TestCase):
  def test_check_positive(self):
    # Test all combinations of test_values and test_types.
    test_values = [-1,0,1,2]
    test_types = [int,float,str]
    for value in test_values:
      for value_type in test_types:
        casted_value = value_type(value)
        if value <= 0:
          with self.assertRaises(argparse.ArgumentTypeError):
            check_positive(casted_value)
        else:
          ret_value = check_positive(casted_value)
          self.assertTrue(isinstance(ret_value,int))
          self.assertTrue(ret_value == value)
  def test_check_fname_exists(self):
    # Create temporary file.
    test_file = tempfile.NamedTemporaryFile(mode='w')
    test_file.write('This is a temporary file used for unit tests.')
    test_file.flush()
    test_filename = test_file.name
    assert os.path.isfile(test_filename)
    self.assertTrue(test_filename == check_fname_exists(test_filename))
    # Closing a temporary file should automatically delete it.
    test_file.close()
    assert not os.path.isfile(test_filename)
    # Test if file checking raises error when file does not exist.
    with self.assertRaises(argparse.ArgumentTypeError):
      check_fname_exists(test_filename)

if __name__ == '__main__':
  unittest.main()