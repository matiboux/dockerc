from . import dir_files
from test.src.reset_dir import reset_dir
from test.src.assert_context import assert_context_found

def test_dev_standard_two(dir_files = dir_files):
    reset_dir('./twd', dir_files)
    assert_context_found(
        'dev',
        (
            b'docker compose' \
            b' -f ./docker-compose.yml' \
            b' -f ./docker-compose.override.yml' \
            b' up -d'
        ),
    )
