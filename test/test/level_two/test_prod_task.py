from test.src.format_dockerc_stdout import format_dockerc_stdout
from test.src.TestDirContext import TestDirContext

def test_prod_task(file = __file__):
    with TestDirContext(file) as ctx:
        dockerc = ctx.run_dockerc(
            'prod.task',
        )
        dockerc.assert_context_ok(
            format_dockerc_stdout(
                b'docker compose' \
                b' -f ./docker-compose.yml' \
                b' -f ./docker-compose.prod.yml' \
                b' -f ./docker-compose.prod.task.yml' \
                b' up -d'
            ),
        )
