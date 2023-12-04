from test.src.reset_dir import reset_dir
from test.src.assert_context import assert_context_not_found

def test_dev_standard_one():
    reset_dir('./cwd', [
        'docker-compose.yml',
    ])
    assert_context_not_found('dev')
