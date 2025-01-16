from test.src.format_dockerc_stdout import format_dockerc_stdout
from test.src.TestDirContext import TestDirContext

def test_dry_run(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'base', 'config',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose-base.yml'
                b' config'
            ),
        )

def test_no_uid(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'base', 'config',
            dry_run = False,
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose-base.yml'
                b' config'
            ) +
            b'name: cwd\n'
            b'services:\n'
            b'  app:\n'
            b'    image: app:latest\n'
            b'    networks:\n'
            b'      default: null\n'
            b'    user: "1001"\n'
            b'networks:\n'
            b'  default:\n'
            b'    name: cwd_default\n'
        )

def test_uid_shell(shell):
    ret = shell.run("sh", "-c", "exit $(id -u)")
    assert ret.returncode == 0

def test_uid(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-u',
            'base', 'config',
            dry_run = False,
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose-base.yml'
                b' config'
            ) +
            b'name: cwd\n'
            b'services:\n'
            b'  app:\n'
            b'    image: app:latest\n'
            b'    networks:\n'
            b'      default: null\n'
            b'    user: "0"\n'
            b'networks:\n'
            b'  default:\n'
            b'    name: cwd_default\n'
        )
