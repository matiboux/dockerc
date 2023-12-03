import subprocess

from src.format_dockerc_stdout import format_dockerc_stdout

def test_default():
    proc = subprocess.Popen(
        ['../../dockerc', '-n'],
        cwd = './test/cwd',
        stdout = subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
    assert stdout == format_dockerc_stdout(
        b'docker compose' \
        b' -f ./docker-compose.yml -f ./docker-compose.override.yml' \
        b' --env-file ./.env --env-file ./.env.local' \
        b' up -d'
    )
    assert stderr == None
    assert proc.returncode == 0
