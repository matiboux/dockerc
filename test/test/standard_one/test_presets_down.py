from test.src.format_dockerc_stdout import format_dockerc_stdout
from test.src.TestDirContext import TestDirContext

def test_presets_d(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@d',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' down'
            )
        )

def test_presets_da(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@da',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' down --remove-orphans'
            )
        )

def test_presets_dr(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@dr',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' down --remove-orphans --rmi local'
            )
        )

def test_presets_dra(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@dra',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' down --remove-orphans --rmi all'
            )
        )

def test_presets_drav(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@drav',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' down --remove-orphans --rmi all -v'
            )
        )

def test_presets_drv(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@drv',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' down --remove-orphans -v'
            )
        )
