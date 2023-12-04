from test.src.reset_dir import reset_dir
from test.src.assert_context import assert_context_found

def test_default_env():
    reset_dir('./cwd', [
        'docker-compose.yml',
        'docker-compose.override.yml',
        '.env',
    ])
    assert_context_found(
        None,
        (
            b'docker compose' \
            b' -f ./docker-compose.yml' \
            b' -f ./docker-compose.override.yml' \
            b' --env-file ./.env' \
            b' up -d'
        ),
    )

def test_default_env_local():
    reset_dir('./cwd', [
        'docker-compose.yml',
        'docker-compose.override.yml',
        '.env.local',
    ])
    assert_context_found(
        None,
        (
            b'docker compose' \
            b' -f ./docker-compose.yml' \
            b' -f ./docker-compose.override.yml' \
            b' --env-file ./.env.local' \
            b' up -d'
        ),
    )

def test_default_env_both():
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
            b' -f ./docker-compose.yml' \
            b' -f ./docker-compose.override.yml' \
            b' --env-file ./.env' \
            b' --env-file ./.env.local' \
            b' up -d'
        ),
    )
