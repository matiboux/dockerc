from src.reset_dir import reset_dir
from src.assert_context import assert_context_not_found, assert_context_found

def test_override_not_found():
    reset_dir('./cwd')
    assert_context_not_found('override')

def test_override_single():
    reset_dir('./cwd', [
        'docker-compose.yml',
    ])
    assert_context_not_found('override')

def test_override_simple():
    reset_dir('./cwd', [
        'docker-compose.yml',
        'docker-compose.override.yml',
    ])
    assert_context_found(
        None,
        (
            b'docker compose' \
            b' -f ./docker-compose.yml -f ./docker-compose.override.yml' \
            b' up -d'
        ),
    )
