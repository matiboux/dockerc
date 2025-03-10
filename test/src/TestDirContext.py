import os
import shutil
import random
import string

from .RunDockerc import RunDockerc

class TestDirContext(object):
    # Tell pytest to ignore this class
    __test__ = False

    def __init__(
        self,
        file: str = __file__,
        dockerc_path: str = None,
    ):
        self.cwd = os.path.join(os.path.dirname(file), 'cwd')
        self.dockerc_path = dockerc_path or os.path.join(os.path.dirname(__file__), '..', '..', 'dockerc')

    def __enter__(self):
        os.makedirs(self.cwd, exist_ok = True)
        return self

    def __exit__(self, *args):
        pass

    def run_dockerc(
        self,
        *args: list[str],
        cwd: str | None = None,
        env: dict[str, str] | None = None,
        dry_run: bool = True,
    ) -> RunDockerc:
        return RunDockerc(
            self.dockerc_path,
            dockerc_args = args,
            cwd = cwd or self.cwd,
            env = env,
            dry_run = dry_run,
        )
