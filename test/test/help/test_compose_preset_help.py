import re

from test.src.TestDirContext import TestDirContext

def test_compose_preset_help(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@',
        )
        dockerc.assert_context_ok(
            re.compile('^Usage:'),
        )
