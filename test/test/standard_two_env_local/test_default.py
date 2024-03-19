from test.src.format_dockerc_stdout import format_dockerc_stdout
from test.src.TestDirContext import TestDirContext

def test_default_env_local(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            None,
        )
        dockerc.assert_context_found(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' -f ./docker-compose.override.yml'
                b' --env-file ./.env.local'
                b' up -d'
            ),
        )
