from src.reset_dir import reset_dir
from src.assert_context import assert_context_not_found, assert_context_found

def test_prod_not_found():
    reset_dir('./cwd')
    assert_context_not_found('prod')

def test_prod_single():
    reset_dir('./cwd', [
        'docker-compose.yml',
    ])
    assert_context_found(
        'prod',
        (
            b'docker compose' \
            b' -f ./docker-compose.yml' \
            b' up -d'
        ),
    )

def test_prod_override():
    reset_dir('./cwd', [
        'docker-compose.yml',
        'docker-compose.override.yml',
    ])
    assert_context_found(
        'prod',
        (
            b'docker compose' \
            b' -f ./docker-compose.yml' \
            b' up -d'
        ),
    )

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
