from . import dir_files
from test.src.reset_dir import reset_dir
from test.src.assert_context import assert_context_not_found

def test_override_not_found():
    reset_dir('./cwd', dir_files)
    assert_context_not_found('override')
