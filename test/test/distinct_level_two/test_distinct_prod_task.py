from . import dir_files
from test.src.reset_dir import reset_dir
from test.src.assert_context import assert_context_found

def test_distinct_prod_task(dir_files = dir_files):
    reset_dir('./cwd', dir_files)
    assert_context_found(
        'distinct.prod.task',
        (
            b'docker compose' \
            b' -f ./docker-compose-distinct.yml' \
            b' -f ./docker-compose-distinct.prod.yml' \
            b' -f ./docker-compose-distinct.prod.task.yml' \
            b' up -d'
        ),
    )
