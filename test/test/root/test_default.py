from test.src.reset_dir import reset_dir
from test.src.assert_context import assert_context_not_found, assert_context_found

def test_default_not_found():
    reset_dir('./cwd')
    assert_context_not_found(None)

def test_default_single():
    reset_dir('./cwd', [
        'docker-compose.yml',
    ])
    assert_context_found(
        None,
        (
            b'docker compose' \
            b' -f ./docker-compose.yml' \
            b' up -d'
        ),
    )

def test_default_override():
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

def test_default_env():
    reset_dir('./cwd', [
        'docker-compose.yml',
        '.env',
    ])
    assert_context_found(
        None,
        (
            b'docker compose' \
            b' -f ./docker-compose.yml' \
            b' --env-file ./.env' \
            b' up -d'
        ),
    )

def test_default_full():
    reset_dir('./cwd', [
        'docker-compose.yml',
        'docker-compose.override.yml',
        '.env',
        '.env.local',
    ])
    assert_context_found(
        None,
        (
            b'docker compose' \
            b' -f ./docker-compose.yml -f ./docker-compose.override.yml' \
            b' --env-file ./.env --env-file ./.env.local' \
            b' up -d'
        ),
    )
