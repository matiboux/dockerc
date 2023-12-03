import subprocess

from src.format_dockerc_stdout import format_dockerc_stdout

def assert_context(
    context: str | None,
    stdout: bytes | None = None,
    stderr: bytes | None = None,
    returncode: int = 0,
) -> None:
    proc = subprocess.Popen(
        (
            ['../dockerc', '-n', context]
            if context is not None
            else ['../dockerc', '-n']
        ),
        cwd = './cwd',
        stdout = subprocess.PIPE,
    )
    stdout, stderr = proc.communicate()
    assert stdout == stdout
    assert stderr == stderr
    assert proc.returncode == returncode

def assert_context_not_found(
    context: str | None,
) -> None:
    assert_context(
        context,
        stdout = (
            (
                b'Error: Unknown context \'' \
                + context.encode('utf-8') \
                + b'\'\n'
            )
            if context is not None
            else (
                b'Error: Default context not found\n'
            )
        ),
        returncode = 1,
    )

def assert_context_found(
    context: str | None,
    stdout: bytes,
) -> None:
    assert_context(
        context,
        stdout = format_dockerc_stdout(stdout),
    )
