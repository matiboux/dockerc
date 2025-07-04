from test.src.format_dockerc_stdout import format_dockerc_stdout
from test.src.TestDirContext import TestDirContext

# def test_default_env(dir_files = dir_files):
#     reset_dir('./twd', dir_files + [
#         '.env',
#     ])
#     assert_context_ok(
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
#     assert_context_ok(
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
#     assert_context_ok(
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
