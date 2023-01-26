# -*- coding: utf-8 -*-
"""Copie para a raiz do projeto antes de usar!"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent

if __name__ == "__main__":
    migrations_dir = ROOT_DIR.rglob('migrations')
    for dirs in migrations_dir:
        for file in dirs.rglob('*.py*'):
            if file.stem != '__init__':
                file.unlink()
                print(f'file {file} removed.')
    print('[!] clean [!]')
