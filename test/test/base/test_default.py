from test.src.TestDirContext import TestDirContext

def test_default_not_found(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            None,
        )
        dockerc.assert_context_not_found()

def test_dev_not_found(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'dev',
        )
        dockerc.assert_context_not_found()

def test_override_not_found(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'override',
        )
        dockerc.assert_context_not_found()

def test_prod_not_found(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'prod',
        )
        dockerc.assert_context_not_found()

def test_what_not_found(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'what',
        )
        dockerc.assert_context_not_found()
