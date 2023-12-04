from . import dir_files
from test.test.none.test_what import test_what as func_test_what
from test.test.none.test_distinct_what import test_distinct_what as func_test_distinct_what

def test_what(dir_files = dir_files):
	func_test_what(dir_files)

def test_distinct_what(dir_files = dir_files):
	func_test_distinct_what(dir_files)
