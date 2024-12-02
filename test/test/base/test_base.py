from test.src.format_dockerc_stdout import format_dockerc_stdout
from test.src.TestDirContext import TestDirContext

def test_base(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'base',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose'
                b' -f ./docker-compose-base.yml'
                b' up -d'
            ),
        )

def test_base_dev_not_found(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'base.dev',
        )
        dockerc.assert_context_not_found()

def test_base_override_not_found(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'base.override',
        )
        dockerc.assert_context_not_found()

def test_base_prod(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'base.prod',
        )
        # !!!
        dockerc.assert_context_not_found()

def test_base_what_not_found(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'base.what',
        )
        dockerc.assert_context_not_found()

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
