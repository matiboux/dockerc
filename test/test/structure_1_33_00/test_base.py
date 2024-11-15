from test.src.format_dockerc_stdout import format_dockerc_stdout
from test.src.TestDirContext import TestDirContext

def test_base(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'base',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose-base.yml'
                b' up -d'
            ),
        )

def test_base_override(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'base.override',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose-base.yml'
                b' -f ./docker-compose-base.override.yml'
                b' up -d'
            ),
        )

def test_base_dev(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'base.dev',
        )
        dockerc.assert_context_not_found()

def test_base_prod_not_found(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'base.prod',
        )
        dockerc.assert_context_not_found()

def test_base_what_not_found(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'base.what',
        )
        dockerc.assert_context_not_found()
