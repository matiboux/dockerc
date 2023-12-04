from test.src.reset_dir import reset_dir
from test.src.assert_context import assert_context_found

def test_prod_simple():
    reset_dir('./cwd', [
        'docker-compose.yml',
        'docker-compose.prod.yml',
    ])
    assert_context_found(
        'prod',
        (
            b'docker compose' \
            b' -f ./docker-compose.yml -f ./docker-compose.prod.yml' \
            b' up -d'
        ),
    )
