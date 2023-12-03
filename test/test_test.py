def test_test():
    assert 3 + 2 == 5

# Test the content of a file
# Path: test/test_file.py
def test_file():
    with open('test/test_file.py') as f:
        assert f.read() == 'def test_file():\n    assert True\n'
