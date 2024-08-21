import re
import subprocess

class RunDockerc():
    def __init__(
        self,
        dockerc_path: str,
        cwd: str,
        context: str | None = None,
        *args: list[str],
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
                *self.args,
            ],
            cwd = self.cwd,
            stdout = subprocess.PIPE,
        )
        self.proc_stdout, self.proc_stderr = self.proc.communicate()

    def assert_context(
        self,
        stdout: bytes | re.Pattern | None = None,
        stderr: bytes | re.Pattern | None = None,
        returncode: int = 0,
    ):
        # if self.proc_stdout != stdout:
        #     # Debugging
        #     import difflib
        #     diff = difflib.unified_diff(
        #         self.proc_stdout.decode('utf-8').splitlines(keepends = True),
        #         (
        #             stdout.decode('utf-8').splitlines(keepends = True)
        #             if isinstance(stdout, bytes) else
        #             stdout.pattern.splitlines(keepends = True)
        #             if isinstance(stdout, re.Pattern) else
        #             stdout
        #         ),
        #     )
        #     print(''.join(diff))

        if isinstance(stdout, re.Pattern):
            assert stdout.match(self.proc_stdout.decode('utf-8'))
        else:
            assert self.proc_stdout == stdout

        if isinstance(stderr, re.Pattern):
            assert stderr.match(self.proc_stderr.decode('utf-8'))
        else:
            assert self.proc_stderr == stderr

        assert self.proc.returncode == returncode

    def assert_context_found(
        self,
        stdout: bytes | re.Pattern = b'',
    ):
        return self.assert_context(
            stdout = stdout,
        )

    def assert_context_error(
        self,
        stdout: bytes | re.Pattern | None = None,
        stderr: bytes | re.Pattern | None = None,
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
