from test.src.format_dockerc_stdout import format_dockerc_stdout
from test.src.TestDirContext import TestDirContext

def test_default_env_both(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc()
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' --env-file ./.env'
                b' --env-file ./.env.local'
                b' up -d'
            ),
        )
