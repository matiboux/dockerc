from test.src.format_dockerc_stdout import format_dockerc_stdout
from test.src.TestDirContext import TestDirContext

def test_abstract_standard(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc()
        dockerc.assert_context_error(
            stdout = b'Error: Abstract context found\n',
        )

def test_abstract_standard_forced(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-f',
        )
        dockerc.assert_context_found(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose.yml'
                b' up -d'
            ),
        )