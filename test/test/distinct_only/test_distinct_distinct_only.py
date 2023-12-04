from test.src.reset_dir import reset_dir
from test.src.assert_context import assert_context_found

def test_distinct_single():
    reset_dir('./cwd', [
        'docker-compose-distinct.yml',
    ])
    assert_context_found(
        'prod',
        (
            b'docker compose' \
            b' -f ./docker-compose-distinct.yml' \
            b' up -d'
        ),
    )
