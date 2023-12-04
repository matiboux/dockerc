from . import dir_files
from test.src.reset_dir import reset_dir
from test.src.assert_context import assert_context_not_found

def test_dev_not_found(dir_files = dir_files):
    reset_dir('./twd', dir_files)
    assert_context_not_found('dev')
