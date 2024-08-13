import subprocess

class RunDockerc():
    def __init__(
        self,
        dockerc_path: str,
        cwd: str,
        context: str | None = None,
        args: str | None = None,
    ):
        self.dockerc_path = dockerc_path
        self.cwd = cwd
        self.context = context
        self.args = args

        self.proc = subprocess.Popen(
            [
                self.dockerc_path,
                '-n',
                *([self.context] if self.context else []),
                *([self.args] if self.args else []),
            ],
            cwd = self.cwd,
            stdout = subprocess.PIPE,
        )
        self.proc_stdout, self.proc_stderr = self.proc.communicate()

    def assert_context(
        self,
        stdout: bytes | None = None,
        stderr: bytes | None = None,
        returncode: int = 0,
    ):
        assert self.proc_stdout == stdout
        assert self.proc_stderr == stderr
        assert self.proc.returncode == returncode

    def assert_context_found(
        self,
        stdout: bytes,
    ):
        return self.assert_context(
            stdout = stdout,
        )

    def assert_context_error(
        self,
        stdout: bytes | None = None,
        stderr: bytes | None = None,
    ):
        return self.assert_context(
            **({'stdout': stdout} if stdout is not None else {}),
            **({'stderr': stderr} if stderr is not None else {}),
            returncode = 1,
        )

    def assert_context_not_found(
        self,
    ):
        return self.assert_context(
            stdout = (
                (
                    b'Error: Unknown context \''
                    + self.context.encode('utf-8')
                    + b'\'\n'
                )
                if self.context is not None else
                (
                    b'Error: Default context not found\n'
                )
            ),
            returncode = 1,
        )
