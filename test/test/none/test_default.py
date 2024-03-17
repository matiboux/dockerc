from test.src.TestDirContext import TestDirContext

def test_default_not_found():
    with TestDirContext() as ctx:
        dockerc = ctx.run_dockerc(
            None,
        )
        dockerc.assert_context_not_found()
