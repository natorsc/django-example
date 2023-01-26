# -*- coding: utf-8 -*-
"""."""

import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent

ENV_SAMPLE = BASE_DIR.joinpath('example.env')

if __name__ == "__main__":
    # create `.env` file in project root
    shutil.copy2(ENV_SAMPLE, ROOT_DIR.joinpath('.env'))
