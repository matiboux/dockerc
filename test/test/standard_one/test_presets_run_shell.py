from test.src.format_dockerc_stdout import format_dockerc_stdout
from test.src.TestDirContext import TestDirContext

def test_presets_sh(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@sh',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' run -i --rm --entrypoint /bin/sh'
            )
        )

def test_presets_shw(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@shw',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' run -w /pwd -v $(pwd):/pwd -i --rm --entrypoint /bin/sh'
            )
        )

def test_presets_dollar(file = __file__):
    return test_presets_shw(file)

def test_presets_dollar_short(file = __file__):
    return test_presets_shw(file)

def test_presets_shb(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@shb',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' run --build -i --rm --entrypoint /bin/sh'
            )
       )

def test_presets_shbw(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@shbw',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' run --build -w /pwd -v $(pwd):/pwd -i --rm --entrypoint /bin/sh'
            )
        )

def test_presets_bash(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@bash',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' run -i --rm --entrypoint /bin/bash'
            )
        )

def test_presets_bashw(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@bashw',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' run -w /pwd -v $(pwd):/pwd -i --rm --entrypoint /bin/bash'
            )
        )

def test_presets_bashb(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@bashb',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' run --build -i --rm --entrypoint /bin/bash'
            )
        )

def test_presets_bashbw(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@bashbw',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' run --build -w /pwd -v $(pwd):/pwd -i --rm --entrypoint /bin/bash'
            )
        )
