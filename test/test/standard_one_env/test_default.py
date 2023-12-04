from . import dir_files
from test.src.reset_dir import reset_dir
from test.src.assert_context import assert_context_found

def test_default_env():
    reset_dir('./cwd', dir_files)
    assert_context_found(
        None,
        (
            b'docker compose' \
            b' -f ./docker-compose.yml' \
            b' --env-file ./.env' \
            b' up -d'
        ),
    )

def test_default_env_local():
    reset_dir('./cwd', [
        'docker-compose.yml',
        '.env.local',
    ])
    assert_context_found(
        None,
        (
            b'docker compose' \
            b' -f ./docker-compose.yml' \
            b' --env-file ./.env.local' \
            b' up -d'
        ),
    )

def test_default_env_both():
    reset_dir('./cwd', dir_files + [
        '.env.local',
    ])
    assert_context_found(
        None,
        (
            b'docker compose' \
            b' -f ./docker-compose.yml' \
            b' --env-file ./.env' \
            b' --env-file ./.env.local' \
            b' up -d'
        ),
    )
