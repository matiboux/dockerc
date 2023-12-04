from test.src.reset_dir import reset_dir
from test.src.assert_context import assert_context_found

def test_prod_two_levels():
    reset_dir('./cwd', [
        'docker-compose.yml',
        'docker-compose.prod.yml',
        'docker-compose.prod.task.yml',
    ])
    assert_context_found(
        'prod.task',
        (
            b'docker compose' \
            b' -f ./docker-compose.yml' \
            b' -f ./docker-compose.prod.yml' \
            b' -f ./docker-compose.prod.task.yml' \
            b' up -d'
        ),
    )
