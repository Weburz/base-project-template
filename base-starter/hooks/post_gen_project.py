#!/usr/bin/env python

"""Script to invoke after the project files/folders are generated."""

import subprocess


def main() -> None:
    """Entrypoint of the script."""
    try:
        subprocess.run(["git", "init"], stdout=subprocess.DEVNULL)
        subprocess.run(
            ["pre-commit", "install", "--install-hooks"], stdout=subprocess.DEVNULL
        )
    except subprocess.CalledProcessError as error:
        raise error


if __name__ == "__main__":
    main()
