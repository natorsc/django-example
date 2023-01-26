# -*- coding: utf-8 -*-
"""."""

import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent


def create_superuser(shell: bool = False) -> None:
    subprocess.call(
        args=['poetry', 'run', 'python', 'manage.py', 'createsuperuser'],
        cwd=ROOT_DIR,
        shell=shell,
    )


if __name__ == "__main__":
    import os

    if os.name == 'nt':
        create_superuser(shell=True)
    else:
        create_superuser()
