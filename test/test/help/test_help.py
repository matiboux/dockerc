import re

from test.src.TestDirContext import TestDirContext

def test_help(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '--help',
        )
        dockerc.assert_context_ok(
            re.compile('^Usage:'),
        )

def test_help_shorthand(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-h',
        )
        dockerc.assert_context_ok(
            re.compile('^Usage:'),
        )
