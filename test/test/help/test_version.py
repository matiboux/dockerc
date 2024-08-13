from test.src.TestDirContext import TestDirContext

VERSION_STDOUT_SHORT = (
    b'DockerC (v1.8.2) - https://github.com/matiboux/dockerc\n'
)

def test_version(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '--version',
        )
        dockerc.assert_context_found(VERSION_STDOUT_SHORT)

def test_version_shorthand(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-v',
        )
        dockerc.assert_context_found(VERSION_STDOUT_SHORT)

def test_version_dry(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-n', '--version',
        )
        dockerc.assert_context_found(VERSION_STDOUT_SHORT)

def test_version_dry_shorthand(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-n', '-v',
        )
        dockerc.assert_context_found(VERSION_STDOUT_SHORT)
