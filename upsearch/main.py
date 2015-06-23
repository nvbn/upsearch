import sys
from itertools import chain
from pathlib import Path


def find_file(path, name):
    for folder in chain.from_iterable([[path], path.parents]):
        file_path = folder.joinpath(name)
        if file_path.is_file():
            return file_path


def main():
    path = Path.cwd()
    file_path = find_file(path, sys.argv[1])
    if file_path:
        print(file_path)
