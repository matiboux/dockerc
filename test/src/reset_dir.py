import os
import shutil

def reset_dir(path: str = './twd', files: list | None = None) -> None:
    shutil.rmtree(path, ignore_errors = True)
    os.makedirs(path, exist_ok = True)

    if files:
        for file in files:
            full_path = os.path.join(path, file)
            os.makedirs(os.path.dirname(full_path), exist_ok = True)
            with open(full_path, 'w') as f:
                f.write('')
