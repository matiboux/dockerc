import re

from test.src.TestDirContext import TestDirContext

def test_update_help(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '--update',
            '--help',
        )
        dockerc.assert_context_ok(
            re.compile('^Usage:'),
        )

def test_update_help_reverse(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '--help',
            '--update',
        )
        dockerc.assert_context_ok(
            re.compile('^Usage:'),
        )

def test_update_help_shorthand(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '--update',
            '-h',
        )
        dockerc.assert_context_ok(
            re.compile('^Usage:'),
        )

def test_update_help_shorthand_reverse(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-h',
            '--update',
        )
        dockerc.assert_context_ok(
            re.compile('^Usage:'),
        )
