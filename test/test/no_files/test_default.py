from test.src.reset_dir import reset_dir
from test.src.assert_context import assert_context_not_found

def test_default_not_found():
    reset_dir('./cwd')
    assert_context_not_found(None)
