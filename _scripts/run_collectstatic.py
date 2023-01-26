# -*- coding: utf-8 -*-
"""."""

import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent

ENV_SAMPLE = BASE_DIR.joinpath('example.env')


def run_collectstatic(shell: bool = False) -> None:
    subprocess.call(
        args=['poetry', 'run', 'python', 'manage.py',
              'collectstatic', '--noinput'],
        cwd=ROOT_DIR,
        shell=shell,
    )


if __name__ == "__main__":
    import os

    if os.name == 'nt':
        run_collectstatic(shell=True)
    else:
        run_collectstatic()
