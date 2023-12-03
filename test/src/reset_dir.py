import os
import shutil

def reset_dir(path = './cwd', files = None):
    shutil.rmtree(path, ignore_errors = True)
    os.makedirs(path)

    if files:
        for file in files:
            with open(os.path.join(path, file), 'w') as f:
                f.write('')
