from test.test.distinct.test_distinct import test_distinct as func_test_distinct
from test.test.empty.test_base import test_base_what_not_found as func_test_distinct_what

def test_distinct(file = __file__):
	func_test_distinct(file)

def test_distinct_what(file = __file__):
	func_test_distinct_what(file)
