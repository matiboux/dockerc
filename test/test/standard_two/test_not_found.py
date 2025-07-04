from test.src.TestDirContext import TestDirContext

def test_what_not_found(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'what',
        )
        dockerc.assert_context_not_found()
