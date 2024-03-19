from test.src.format_dockerc_stdout import format_dockerc_stdout
from test.src.TestDirContext import TestDirContext

def test_base_prod(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'base.prod',
        )
        dockerc.assert_context_found(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose-base.yml'
                b' -f ./docker-compose-base.prod.yml'
                b' up -d'
            ),
        )

def test_base_prod_sub_not_found(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'base.prod.sub',
        )
        dockerc.assert_context_not_found()

def test_base_prod_what_not_found(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'base.prod.what',
        )
        dockerc.assert_context_not_found()
