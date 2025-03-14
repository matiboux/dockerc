from test.src.format_dockerc_stdout import format_dockerc_stdout
from test.src.TestDirContext import TestDirContext

def test_prod_simple(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'prod',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose' \
                b' -f ./docker-compose.yml -f ./docker-compose.prod.yml' \
                b' up -d'
            ),
        )
