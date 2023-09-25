#!/usr/bin/env python

"""Script to invoke after the project files/folders are generated."""

import subprocess


def main() -> None:
    """Entrypoint of the script."""
    message = """
        Project generation complete...run the following commands now:

        "npm run dev" to start the development server and open the website at "http://localhost:3000".
    """

    try:
        subprocess.run(["git", "init"], stdout=subprocess.DEVNULL)
        subprocess.run(["npm", "install"])
        print(message)
    except subprocess.CalledProcessError as error:
        raise error


if __name__ == "__main__":
    main()
