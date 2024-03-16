import os
import shutil
import random
import string

TEST_DIR_PREFIX = os.path.abspath('./twd')

class WorkingDirTest(object):
    def __init__(self, test_name: str):
        # Generate a random suffix to avoid conflicts
        random_suffix = ''.join(random.choice(string.ascii_lowercase + string.digits) for i in range(8))
        test_dir_name = f"{test_name}_{random_suffix}"
        self.dir_path = os.path.join(TEST_DIR_PREFIX, test_dir_name)

    def __enter__(self):
        os.makedirs(self.dir_path, exist_ok = True)
        return self

    def __exit__(self, *args):
        shutil.rmtree(self.dir_path, ignore_errors = True)

    def add_file(self, file_name: str, content: str = '') -> None:
        if not file_name:
            return
        full_path = os.path.join(self.dir_path, file_name)
        os.makedirs(os.path.dirname(full_path), exist_ok = True)
        with open(full_path, 'w') as f:
            f.write(content)

    def add_empty_files(self, *file_names: str) -> None:
        if len(file_names) < 1:
            return
        for file_name in file_names:
            self.add_file(file_name)
