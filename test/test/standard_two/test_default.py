from test.src.format_dockerc_stdout import format_dockerc_stdout
from test.src.TestDirContext import TestDirContext

def test_default(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            None,
        )
        dockerc.assert_context_found(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' -f ./docker-compose.override.yml'
                b' up -d'
            ),
        )

def test_dev_not_found(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'dev',
        )
        dockerc.assert_context_found(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' -f ./docker-compose.override.yml'
                b' up -d'
            ),
        )

def test_override_not_found(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'override',
        )
        dockerc.assert_context_found(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' -f ./docker-compose.override.yml'
                b' up -d'
            ),
        )

def test_prod_not_found(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'prod',
        )
        dockerc.assert_context_found(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up -d'
            ),
        )

def test_what_not_found(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'what',
        )
        dockerc.assert_context_not_found()

# def test_default_env(dir_files = dir_files):
#     reset_dir('./twd', dir_files + [
#         '.env',
#     ])
#     assert_context_found(
#         None,
#         (
#             b'docker compose' \
#             b' -f ./docker-compose.yml' \
#             b' -f ./docker-compose.override.yml' \
#             b' --env-file ./.env' \
#             b' up -d'
#         ),
#     )

# def test_default_env_local(dir_files = dir_files):
#     reset_dir('./twd', dir_files + [
#         '.env.local',
#     ])
#     assert_context_found(
#         None,
#         (
#             b'docker compose' \
#             b' -f ./docker-compose.yml' \
#             b' -f ./docker-compose.override.yml' \
#             b' --env-file ./.env.local' \
#             b' up -d'
#         ),
#     )

# def test_default_env_both():
#     reset_dir('./twd', dir_files + [
#         '.env',
#         '.env.local',
#     ])
#     assert_context_found(
#         None,
#         (
#             b'docker compose' \
#             b' -f ./docker-compose.yml' \
#             b' -f ./docker-compose.override.yml' \
#             b' --env-file ./.env' \
#             b' --env-file ./.env.local' \
#             b' up -d'
#         ),
#     )
