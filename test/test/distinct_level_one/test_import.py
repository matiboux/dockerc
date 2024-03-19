from . import dir_files
from test.test.distinct.test_distinct import test_distinct as func_test_distinct
from test.test.empty.test_base import test_base_what_not_found as func_test_distinct_what

def test_distinct(dir_files = dir_files):
	func_test_distinct(dir_files)

def test_distinct_what(file = __file__):
	func_test_distinct_what(file)
