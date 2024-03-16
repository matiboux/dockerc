import subprocess

from test.src.format_dockerc_stdout import format_dockerc_stdout

def assert_context(
    context: str | None,
    stdout: bytes | None = None,
    stderr: bytes | None = None,
    returncode: int = 0,
    dockerc_path: str = '../dockerc',
    cwd: str = './twd',
) -> None:
    proc = subprocess.Popen(
        (
            [dockerc_path, '-n', context]
            if context is not None
            else [dockerc_path, '-n']
        ),
        cwd = cwd,
        stdout = subprocess.PIPE,
    )
    proc_stdout, proc_stderr = proc.communicate()
    assert proc_stdout == stdout
    assert proc_stderr == stderr
    assert proc.returncode == returncode

def assert_context_not_found(
    context: str | None,
    dockerc_path: str = None,
    cwd: str = None,
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
        **({ 'dockerc_path': dockerc_path } if dockerc_path else {}),
        **({ 'cwd': cwd } if cwd else {}),
    )

def assert_context_found(
    context: str | None,
    stdout: bytes,
    dockerc_path: str = None,
    cwd: str = None,
) -> None:
    assert_context(
        context,
        stdout = format_dockerc_stdout(stdout),
        **({ 'dockerc_path': dockerc_path } if dockerc_path else {}),
        **({ 'cwd': cwd } if cwd else {}),
    )
