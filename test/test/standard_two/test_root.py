from test.src.format_dockerc_stdout import format_dockerc_stdout
from test.src.TestDirContext import TestDirContext

def test_root(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '.',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up -d'
            ),
        )

def test_prod(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'prod',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up -d'
            ),
        )
