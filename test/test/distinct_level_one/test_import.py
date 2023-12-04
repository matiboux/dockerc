from . import dir_files
from test.test.distinct.test_distinct import test_distinct as func_test_distinct
from test.test.none.test_distinct_what import test_distinct_what as func_test_distinct_what

def test_distinct(dir_files = dir_files):
	func_test_distinct(dir_files)

def test_distinct_what(dir_files = dir_files):
	func_test_distinct_what(dir_files)
