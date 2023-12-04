from . import dir_files
from test.test.distinct.test_distinct import test_distinct as func_test_distinct

def test_distinct(dir_files = dir_files):
	func_test_distinct(dir_files)
