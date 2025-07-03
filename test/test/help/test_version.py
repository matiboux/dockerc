import re

from test.src.TestDirContext import TestDirContext

VERSION_STDOUT_SHORT_REGEX = (
    r'^DockerC \(v[0-9]+\.[0-9]+\.[0-9]+\) - https://github\.com/matiboux/dockerc\n$'
)

def test_version(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '--version',
        )
        dockerc.assert_context_ok(
            re.compile(VERSION_STDOUT_SHORT_REGEX)
        )

def test_version_shorthand(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-v',
        )
        dockerc.assert_context_ok(
            re.compile(VERSION_STDOUT_SHORT_REGEX)
        )

def test_version_dry(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-n', '--version',
        )
        dockerc.assert_context_ok(
            re.compile(VERSION_STDOUT_SHORT_REGEX)
        )

def test_version_dry_shorthand(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-n', '-v',
        )
        dockerc.assert_context_ok(
            re.compile(VERSION_STDOUT_SHORT_REGEX)
        )
