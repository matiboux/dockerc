import re
import subprocess

class RunDockerc():
    def __init__(
        self,
        dockerc_path: str,
        dockerc_args: list[str],
        cwd: str,
        context: str | None = None,
        env: dict[str, str] | None = None,
    ):
        self.dockerc_path = dockerc_path
        self.dockerc_args = dockerc_args
        self.cwd = cwd
        self.context = (
            context
            if context is not None else
            dockerc_args[0]
            if dockerc_args and not dockerc_args[0].startswith('-') else
            None
        )
        self.env = env

        self.proc = subprocess.Popen(
            [
                self.dockerc_path,
                '-n',
                *self.dockerc_args,
            ],
            cwd = self.cwd,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            env = self.env,
        )
        self.proc_stdout, self.proc_stderr = self.proc.communicate()

    def assert_context(
        self,
        *,
        stdout: bytes | re.Pattern | None = b'',
        stderr: bytes | re.Pattern | None = b'',
        returncode: int = 0,
    ):
        if stdout is not None:
            if self.proc_stdout != stdout:
                # Debugging
                import difflib
                diff = difflib.unified_diff(
                    self.proc_stdout.decode('utf-8').splitlines(keepends = True),
                    (
                        stdout.decode('utf-8').splitlines(keepends = True)
                        if isinstance(stdout, bytes) else
                        stdout.pattern.splitlines(keepends = True)
                        if isinstance(stdout, re.Pattern) else
                        stdout
                    ),
                )
                print(''.join(diff))

            if isinstance(stdout, re.Pattern):
                assert stdout.match(self.proc_stdout.decode('utf-8'))
            else:
                assert self.proc_stdout == stdout

        if stderr is not None:
            if self.proc_stderr != stderr:
                # Debugging
                import difflib
                diff = difflib.unified_diff(
                    self.proc_stderr.decode('utf-8').splitlines(keepends = True),
                    (
                        stderr.decode('utf-8').splitlines(keepends = True)
                        if isinstance(stderr, bytes) else
                        stderr.pattern.splitlines(keepends = True)
                        if isinstance(stderr, re.Pattern) else
                        stderr
                    ),
                )
                print(''.join(diff))

            if isinstance(stderr, re.Pattern):
                assert stderr.match(self.proc_stderr.decode('utf-8'))
            else:
                assert self.proc_stderr == stderr

        assert self.proc.returncode == returncode

    def assert_context_ok(
        self,
        stdout: bytes | re.Pattern = b'',
        *,
        stderr: bytes | re.Pattern | None = None,
    ):
        return self.assert_context(
            stdout = stdout,
            **({'stderr': stderr} if stderr is not None else {}),
        )

    def assert_context_error(
        self,
        stderr: bytes | re.Pattern | None = None,
        *,
        stdout: bytes | re.Pattern | None = None,
        returncode: int = 1,
    ):
        return self.assert_context(
            **({'stdout': stdout} if stdout is not None else {}),
            **({'stderr': stderr} if stderr is not None else {}),
            returncode = returncode,
        )

    def assert_context_not_found(
        self,
    ):
        return self.assert_context(
            stderr = (
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
