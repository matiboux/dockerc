import os
import shutil
import random
import string

import assert_context

class TestDirContext(object):
    # Tell pytest to ignore this class
    __test__ = False

    def __init__(
        self,
        file: str = __file__,
        dockerc_path: str = None,
    ):
        self.test_cwd = os.path.join(os.path.dirname(file), 'cwd')
        self.dockerc_path = dockerc_path or os.path.join(os.path.dirname(file), '..', '..', 'dockerc')

    def __enter__(self):
        os.makedirs(self.test_cwd, exist_ok = True)
        return self

    def __exit__(self, *args):
        pass

    def assert_context(
        self,
        context: str | None,
        stdout: bytes | None = None,
        stderr: bytes | None = None,
        returncode: int = 0,
    ) -> None:
        return assert_context.assert_context(
            context,
            stdout = stdout,
            stderr = stderr,
            returncode = returncode,
            dockerc_path = self.dockerc_path,
            cwd = self.test_cwd,
        )

    def assert_context_not_found(
        self,
        context: str | None,
    ) -> None:
        return assert_context.assert_context_not_found(
            context,
            dockerc_path = self.dockerc_path,
            cwd = self.test_cwd,
        )

    def assert_context_found(
        self,
        context: str | None,
        stdout: bytes,
    ) -> None:
        return assert_context.assert_context_found(
            context,
            stdout,
            dockerc_path = self.dockerc_path,
            cwd = self.test_cwd,
        )
