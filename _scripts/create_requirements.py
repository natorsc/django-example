# -*- coding: utf-8 -*-
"""Script used to automate the creation of `requirements.txt` files."""

import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent

REQUIREMENTS_FILE = ROOT_DIR.joinpath('requirements.txt')
REQUIREMENTS_DEV_FILE = ROOT_DIR.joinpath('requirements-dev.txt')
REQUIREMENTS_DOCS_FILE = ROOT_DIR.joinpath('requirements-docs.txt')


def create_requirements(shell: bool = False) -> None:
    subprocess.call(
        args=['poetry', 'export', '--without-hashes', '-f', 'requirements.txt',
              '-o', f'{REQUIREMENTS_FILE}'],
        cwd=ROOT_DIR,
        shell=shell,
    )


def create_requirements_dev(shell: bool = False) -> None:
    subprocess.call(
        args=['poetry', 'export', '--with', 'dev', '--without-hashes',
              '-f', 'requirements.txt', '-o', f'{REQUIREMENTS_DEV_FILE}'],
        cwd=ROOT_DIR,
        shell=shell,
    )


def create_requirements_docs(shell: bool = False) -> None:
    subprocess.call(
        args=['poetry', 'export', '--with', 'docs', '--without-hashes',
              '-f', 'requirements.txt', '-o', f'{REQUIREMENTS_DOCS_FILE}'],
        cwd=ROOT_DIR,
        shell=shell,
    )


if __name__ == "__main__":
    import os

    if os.name == 'nt':
        create_requirements(shell=True)
        create_requirements_dev(shell=True)
    else:
        create_requirements()
        create_requirements_dev()
