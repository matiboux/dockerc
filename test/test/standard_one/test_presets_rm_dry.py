from test.src.format_dockerc_stdout import format_dockerc_stdout
from test.src.TestDirContext import TestDirContext

def test_presets_rs(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-n', '-', '@rs',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' rm --stop'
            )
        )

def test_presets_rf(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-n', '-', '@rf',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' rm -f'
            )
        )

def test_presets_rfv(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-n', '-', '@rfv',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' rm -f -v'
            )
        )
