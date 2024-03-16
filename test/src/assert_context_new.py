import subprocess

from test.src.format_dockerc_stdout import format_dockerc_stdout
from test.src.WorkingDirTest import WorkingDirTest

def assert_context(
    twd: WorkingDirTest,
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
        cwd = twd.dir_path,
        stdout = subprocess.PIPE,
    )
    proc_stdout, proc_stderr = proc.communicate()
    assert proc_stdout == stdout
    assert proc_stderr == stderr
    assert proc.returncode == returncode

def assert_context_not_found(
    twd: WorkingDirTest,
    context: str | None,
) -> None:
    assert_context(
        twd,
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
    twd: WorkingDirTest,
    context: str | None,
    stdout: bytes,
) -> None:
    assert_context(
        twd,
        context,
        stdout = format_dockerc_stdout(stdout),
    )
