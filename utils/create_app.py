import pathlib
import shutil
import os
from pathlib import Path
import sys

# PROJECT_DIR = os.getcwd()

def create_package():
    package_name = sys.argv[1]
    if package_name is None or package_name.strip() == "":
        return

    os.mkdir(package_name)


def create_app():
    if len(sys.argv) <= 1:
        return

    package_name = sys.argv[1]
    if not os.path.isdir(sys.argv[1]):
        create_package()

    source_file = f"{package_name}.py"
    files_to_create= [
        "main.py", "tests.py", "base.py", "__init__.py", source_file
    ]

    for file in files_to_create:
        with open(f"{package_name}/{file}", "w") as e:
            pass


if __name__ == "__main__":
    create_app()

