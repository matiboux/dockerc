from . import dir_files
from test.src.reset_dir import reset_dir
from test.src.assert_context import assert_context_found

def test_default_standard_one():
    reset_dir('./cwd', dir_files)
    assert_context_found(
        None,
        (
            b'docker compose' \
            b' -f ./docker-compose.yml' \
            b' up -d'
        ),
    )
