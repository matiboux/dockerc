import re

from test.src.TestDirContext import TestDirContext

def test_help_args_presets(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            '-', '@',
        )
        dockerc.assert_context_ok(
            re.compile('^Usage:'),
        )
