from . import dir_files
from test.src.reset_dir import reset_dir
from test.src.assert_context import assert_context_found

def test_override_standard_two():
    reset_dir('./cwd', dir_files)
    assert_context_found(
        'override',
        (
            b'docker compose' \
            b' -f ./docker-compose.yml' \
            b' -f ./docker-compose.override.yml' \
            b' up -d'
        ),
    )
