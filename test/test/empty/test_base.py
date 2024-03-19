from test.src.TestDirContext import TestDirContext

def test_base_not_found():
    with TestDirContext(__file__) as ctx:
        dockerc = ctx.run_dockerc(
            'base',
        )
        dockerc.assert_context_not_found()

def test_base_dev_not_found():
    with TestDirContext(__file__) as ctx:
        dockerc = ctx.run_dockerc(
            'base.dev',
        )
        dockerc.assert_context_not_found()

def test_base_override_not_found():
    with TestDirContext(__file__) as ctx:
        dockerc = ctx.run_dockerc(
            'base.override',
        )
        dockerc.assert_context_not_found()

def test_base_prod_not_found():
    with TestDirContext(__file__) as ctx:
        dockerc = ctx.run_dockerc(
            'base.prod',
        )
        dockerc.assert_context_not_found()

def test_base_what_not_found():
    with TestDirContext(__file__) as ctx:
        dockerc = ctx.run_dockerc(
            'base.what',
        )
        dockerc.assert_context_not_found()
