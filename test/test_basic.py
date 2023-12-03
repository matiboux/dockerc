import subprocess

from src.format_dockerc_stdout import format_dockerc_stdout

# Test the DockerC script runs
def test_basic():
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
