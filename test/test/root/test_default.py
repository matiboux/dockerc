import subprocess

from src.reset_dir import reset_dir
from src.format_dockerc_stdout import format_dockerc_stdout

def test_default_not_found():
    reset_dir('./cwd')
    proc = subprocess.Popen(
        ['../dockerc', '-n'],
        cwd = './cwd',
        stdout = subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
    assert stdout == (
        b'Error: Default context not found\n'
    )
    assert stderr == None
    assert proc.returncode == 1

def test_default_single():
    reset_dir('./cwd', [
        'docker-compose.yml',
    ])
    proc = subprocess.Popen(
        ['../dockerc', '-n'],
        cwd = './cwd',
        stdout = subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
    assert stdout == format_dockerc_stdout(
        b'docker compose' \
        b' -f ./docker-compose.yml' \
        b' up -d'
    )
    assert stderr == None
    assert proc.returncode == 0

def test_default_override():
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

def test_default_env():
    reset_dir('./cwd', [
        'docker-compose.yml',
        '.env',
    ])
    proc = subprocess.Popen(
        ['../dockerc', '-n'],
        cwd = './cwd',
        stdout = subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
    assert stdout == format_dockerc_stdout(
        b'docker compose' \
        b' -f ./docker-compose.yml' \
        b' --env-file ./.env' \
        b' up -d'
    )
    assert stderr == None
    assert proc.returncode == 0

def test_default_full():
    reset_dir('./cwd', [
        'docker-compose.yml',
        'docker-compose.override.yml',
        '.env',
        '.env.local',
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
        b' --env-file ./.env --env-file ./.env.local' \
        b' up -d'
    )
    assert stderr == None
    assert proc.returncode == 0
