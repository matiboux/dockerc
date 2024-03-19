from test.test.empty.test_default import test_what_not_found as func_test_what_not_found
from test.test.empty.test_base import test_base_not_found as func_test_base_not_found

def test_what_not_found(file = __file__):
	func_test_what_not_found(file)

def test_base_not_found(file = __file__):
	func_test_base_not_found(file)
