import os
import shutil
import random
import string

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
