from test.src.format_dockerc_stdout import format_dockerc_stdout
from test.src.TestDirContext import TestDirContext

def test_default_config_syntax_error(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            None,
            'config',
        )
        dockerc.assert_context_error(
            stdout = b'Error: Unknown context \'config\'\n',
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
