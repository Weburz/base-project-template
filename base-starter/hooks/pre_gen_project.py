#!/usr/bin/env python3

"""Script to run before generating the project structure."""

import subprocess


def main() -> None:
    """Entrypoint of the script."""
    try:
        subprocess.run(["git", "--version"], stdout=subprocess.DEVNULL)
        subprocess.run(["pre-commit", "--version"], stdout=subprocess.DEVNULL)
    except subprocess.CalledProcessError as error:
        raise error


if __name__ == "__main__":
    main()
