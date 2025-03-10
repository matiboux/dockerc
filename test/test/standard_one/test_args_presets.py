from test.src.format_dockerc_stdout import format_dockerc_stdout
from test.src.TestDirContext import TestDirContext

def test_default_u(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-',
            '@u',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up -d'
            ),
        )

def test_default_ub(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-',
            '@ub',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up --build -d'
            ),
        )

def test_default_uf(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-',
            '@uf',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up --force-recreate -d'
            ),
        )

def test_default_ubf(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-',
            '@ubf',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up --build --force-recreate -d'
            ),
        )

def test_default_uabc(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-',
            '@uabc',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up --build'
            ),
            stderr = (
                b'Warning: Unknown compose up preset character \'c\'\n'
            )
        )
