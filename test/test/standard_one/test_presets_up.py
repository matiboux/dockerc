from test.src.format_dockerc_stdout import format_dockerc_stdout
from test.src.TestDirContext import TestDirContext

def test_presets_u(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@u',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up -d'
            )
        )

def test_presets_ua(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@ua',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up'
            )
        )

def test_presets_ub(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@ub',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up --build -d'
            )
        )

def test_presets_uba(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@uba',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up --build'
            )
        )

def test_presets_ubf(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@ubf',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up --build -d --force-recreate'
            )
        )

def test_presets_ubfa(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@ubfa',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up --build --force-recreate'
            )
        )

def test_presets_ubfp(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@ubfp',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up --build -d --force-recreate --pull always'
            )
        )

def test_presets_ubfap(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@ubfap',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up --build --force-recreate --pull always'
            )
        )

def test_presets_ubr(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@ubr',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up --build -d --remove-orphans'
            )
        )

def test_presets_ubar(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@ubar',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up --build --remove-orphans'
            )
        )

def test_presets_ubfr(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@ubfr',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up --build -d --force-recreate --remove-orphans'
            )
        )

def test_presets_ubfar(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@ubfar',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up --build --force-recreate --remove-orphans'
            )
        )

def test_presets_uf(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@uf',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up -d --force-recreate'
            )
        )

def test_presets_ufa(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@ufa',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up --force-recreate'
            )
        )

def test_presets_ur(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@ur',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up -d --remove-orphans'
            )
        )

def test_presets_uar(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@uar',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up --remove-orphans'
            )
        )

def test_presets_ufr(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@ufr',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up -d --force-recreate --remove-orphans'
            )
        )

def test_presets_ufar(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@ufar',
        )
        dockerc.assert_context(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up --force-recreate --remove-orphans'
            )
        )
