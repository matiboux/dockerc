from test.src.format_dockerc_stdout import format_dockerc_stdout
from test.src.TestDirContext import TestDirContext

def test_default():
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

def test_dev_not_found():
    with TestDirContext(__file__) as ctx:
        dockerc = ctx.run_dockerc(
            'dev',
        )
        dockerc.assert_context_not_found()

def test_override_not_found():
    with TestDirContext(__file__) as ctx:
        dockerc = ctx.run_dockerc(
            'override',
        )
        dockerc.assert_context_not_found()

def test_prod_not_found():
    with TestDirContext(__file__) as ctx:
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

def test_what_not_found():
    with TestDirContext(__file__) as ctx:
        dockerc = ctx.run_dockerc(
            'what',
        )
        dockerc.assert_context_not_found()
