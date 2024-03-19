from test.test.empty.test_default import test_what_not_found as func_test_what
from test.test.empty.test_base import test_base_not_found as func_test_distinct

def test_what(file = __file__):
	func_test_what(file)

def test_distinct(file = __file__):
	func_test_distinct(file)
