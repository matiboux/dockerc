from . import dir_files
from test.src.WorkingDirTest import WorkingDirTest
from test.src.assert_context_new import assert_context_not_found

def test_default_not_found(dir_files = dir_files):
    with WorkingDirTest('test_default_not_found') as twd:
        twd.add_empty_files(dir_files)
        assert_context_not_found(twd, None)
