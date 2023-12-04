from . import dir_files
from test.src.reset_dir import reset_dir
from test.src.assert_context import assert_context_found

def test_prod_standard_two(dir_files = dir_files):
    reset_dir('./twd', dir_files)
    assert_context_found(
        'prod',
        (
            b'docker compose' \
            b' -f ./docker-compose.yml' \
            b' up -d'
        ),
    )
