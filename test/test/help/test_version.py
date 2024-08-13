from test.src.TestDirContext import TestDirContext

VERSION_STDOUT = (
    b'DockerC (v1.8.2) - https://github.com/matiboux/dockerc\n'
    b'Notice: DockerC is not up to date, latest version is !\n'
)

def test_version(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '--version',
        )
        dockerc.assert_context_found(VERSION_STDOUT)

def test_version_shorthand(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-v',
        )
        dockerc.assert_context_found(VERSION_STDOUT)
