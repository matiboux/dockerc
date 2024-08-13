import subprocess

from test.src.reset_dir import reset_dir

VERSION_STDOUT = (
    b'DockerC (v1.8.2) - https://github.com/matiboux/dockerc\n'
    b'Notice: DockerC is not up to date, latest version is !\n'
)

def test_version():
    reset_dir('./twd')
    proc = subprocess.Popen(
        ['../dockerc', '--version'],
        cwd = './twd',
        stdout = subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
    assert stdout == VERSION_STDOUT
    assert stderr == None
    assert proc.returncode == 0

def test_version_shorthand():
    reset_dir('./twd')
    proc = subprocess.Popen(
        ['../dockerc', '-v'],
        cwd = './twd',
        stdout = subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
    assert stdout == VERSION_STDOUT
    assert stderr == None
    assert proc.returncode == 0
