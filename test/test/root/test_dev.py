import subprocess

from src.reset_dir import reset_dir
from src.format_dockerc_stdout import format_dockerc_stdout

def test_dev_not_found():
    reset_dir('./cwd')
    proc = subprocess.Popen(
        ['../dockerc', '-n', 'dev'],
        cwd = './cwd',
        stdout = subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
    assert stdout == (
        b'Error: Unknown context \'dev\'\n'
    )
    assert stderr == None
    assert proc.returncode == 1

def test_dev_single():
    reset_dir('./cwd', [
        'docker-compose.yml',
    ])
    proc = subprocess.Popen(
        ['../dockerc', '-n', 'dev'],
        cwd = './cwd',
        stdout = subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
    assert stdout == (
        b'Error: Unknown context \'dev\'\n'
    )
    assert stderr == None
    assert proc.returncode == 1

def test_dev_override():
    reset_dir('./cwd', [
        'docker-compose.yml',
        'docker-compose.override.yml',
    ])
    proc = subprocess.Popen(
        ['../dockerc', '-n'],
        cwd = './cwd',
        stdout = subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
    assert stdout == format_dockerc_stdout(
        b'docker compose' \
        b' -f ./docker-compose.yml -f ./docker-compose.override.yml' \
        b' up -d'
    )
    assert stderr == None
    assert proc.returncode == 0
