from . import dir_files
from test.test.none.test_distinct_prod import test_distinct_prod as func_test_distinct_prod
from test.test.none.test_distinct_what import test_distinct_what as func_test_distinct_what

def test_distinct_prod(dir_files = dir_files):
	func_test_distinct_prod(dir_files)

def test_distinct_what(dir_files = dir_files):
	func_test_distinct_what(dir_files)
