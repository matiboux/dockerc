from test.src.reset_dir import reset_dir
from test.src.assert_context import assert_context_found

def test_distinct_single():
    reset_dir('./cwd', [
        'docker-compose-distinct.yml',
        'docker-compose-distinct.prod.yml',
    ])
    assert_context_found(
        'distinct.prod',
        (
            b'docker compose' \
            b' -f ./docker-compose-distinct.yml' \
            b' -f ./docker-compose-distinct.prod.yml' \
            b' up -d'
        ),
    )
