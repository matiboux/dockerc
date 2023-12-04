from . import dir_files
from test.src.reset_dir import reset_dir
from test.src.assert_context import assert_context_found

def test_default(dir_files = dir_files):
    reset_dir('./cwd', dir_files)
    assert_context_found(
        None,
        (
            b'docker compose' \
            b' -f ./docker-compose.yml' \
            b' -f ./docker-compose.override.yml' \
            b' up -d'
        ),
    )

def test_default_env(dir_files = dir_files):
    reset_dir('./cwd', dir_files + [
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

def test_default_env_local(dir_files = dir_files):
    reset_dir('./cwd', dir_files + [
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
    reset_dir('./cwd', dir_files + [
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
