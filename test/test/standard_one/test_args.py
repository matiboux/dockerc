from test.src.format_dockerc_stdout import format_dockerc_stdout
from test.src.TestDirContext import TestDirContext

def test_default_config_syntax_error(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'config',
        )
        dockerc.assert_context_error(
            stderr = b'Error: Unknown context \'config\'\n',
        )

def test_default_config(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-',
            'config',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' config'
            ),
        )

def test_exec(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '@exec',
            'container_name',
            'command',
        )
        dockerc.assert_exec(
            'container_name',
            'command',
        )

def test_execi(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '@execi',
            'container_name',
            'command',
        )
        dockerc.assert_execi(
            'container_name',
            'command',
        )

def test_execd(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '@execd',
            'container_name',
            'command',
        )
        dockerc.assert_execd(
            'container_name',
            'command',
        )
