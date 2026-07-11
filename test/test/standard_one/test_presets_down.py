from test.src.format_dockerc_stdout import format_dockerc_stdout
from test.src.TestDirContext import TestDirContext

def test_presets_d(file = __file__):
    # Down (basic)
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@d',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' down'
            )
        )

def test_presets_da(file = __file__):
    # Down with remove level 1
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@da',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' down --remove-orphans'
            )
        )

def test_presets_dr(file = __file__):
    # Down with remove level 2
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@dr',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' down --remove-orphans --rmi local'
            )
        )

def test_presets_dar(file = __file__):
    # Down with remove level 2
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@dar',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' down --remove-orphans --rmi local'
            )
        )

def test_presets_dra(file = __file__):
    # Down with remove level 3
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@dra',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' down --remove-orphans --rmi all'
            )
        )

def test_presets_dv(file = __file__):
    # Down with volumes
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@dv',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' down -v'
            )
        )

def test_presets_drav(file = __file__):
    # Down with remove level 3 and volumes
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@drav',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' down --remove-orphans --rmi all -v'
            )
        )

def test_presets_drv(file = __file__):
    # Down with remove level 2 and volumes
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@drv',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' down --remove-orphans --rmi local -v'
            )
        )

def test_presets_dav(file = __file__):
    # Down with remove level 1 and volumes
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@dav',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' down --remove-orphans -v'
            )
        )

def test_presets_darv(file = __file__):
    # Down with remove level 2 and volumes
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@darv',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' down --remove-orphans --rmi local -v'
            )
        )
