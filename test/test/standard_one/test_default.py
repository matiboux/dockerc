from . import dir_files
from test.src.reset_dir import reset_dir
from test.src.assert_context import assert_context_found
from test.src.format_dockerc_stdout import format_dockerc_stdout
from test.src.TestDirContext import TestDirContext

def test_default_new():
    with TestDirContext(__file__) as ctx:
        dockerc = ctx.run_dockerc(
            None,
        )
        dockerc.assert_context_found(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up -d'
            ),
        )

def test_default(dir_files = dir_files):
    reset_dir('./twd', dir_files)
    assert_context_found(
        None,
        (
            b'docker compose' \
            b' -f ./docker-compose.yml' \
            b' up -d'
        ),
    )

def test_default_env(dir_files = dir_files):
    reset_dir('./twd', dir_files + [
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

def test_default_env_local(dir_files = dir_files):
    reset_dir('./twd', dir_files + [
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

def test_default_env_both(dir_files = dir_files):
    reset_dir('./twd', dir_files + [
        '.env',
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
