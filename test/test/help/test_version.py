import subprocess

from src.format_dockerc_stdout import format_dockerc_stdout

VERSION_STDOUT = (
    b'DockerC (v1.8.2) - https://github.com/matiboux/dockerc\n'
    b'Notice: DockerC is not up to date, latest version is !\n'
)

def test_version():
    proc = subprocess.Popen(
        ['../../dockerc', '--version'],
        cwd = './test/cwd',
        stdout = subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
    assert stdout == VERSION_STDOUT
    assert stderr == None
    assert proc.returncode == 0

def test_version_shorthand():
    proc = subprocess.Popen(
        ['../../dockerc', '-v'],
        cwd = './test/cwd',
        stdout = subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
    assert stdout == VERSION_STDOUT
    assert stderr == None
    assert proc.returncode == 0
