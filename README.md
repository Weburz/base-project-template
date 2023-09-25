# Weburz's Project Starters

[![QA Checks](https://github.com/Weburz/cookiecutter-templates/actions/workflows/qa-check.yml/badge.svg)](https://github.com/Weburz/cookiecutter-templates/actions/workflows/qa-check.yml)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Weburz/cookiecutter-templates?logo=github&label=Repo%20Size)

This repository contains a bunch of templates to quickly generate projects at
Weburz. It contains the base skeleton resources required for any and all
projects built within Weburz. Hence, this repository should ideally be used to
generate repositories for other future projects in Weburz.

More information about this repository will be added as and when necessary!

## Usage Guidelines

This template repository is supposed to be used with
[`cookiecutter`](https://cookiecutter.readthedocs.io) to generate a template
repository to start work on at Weburz. Hence, to get started with using the
repository;

1. Ensure you have `cookiecutter` installed (if not follow the guidelines as
   stated in the documentation linked above).
2. Run the following command to generate a template repository with all the
   necessary skeleton files.

   ```console
   cookiecutter gh:Weburz/project-starters
   ```

3. With that you will be prompted to select the right template, so choose the
   appropriate template before starting work with it.

With the project generated, change the directory in to the project's directory
and start working on it as you deem it fit to.

## Development Guidelines

If you have an idea for a template or want to make some improvements to the
current set of templates, please feel free to do so. But before you share a PR
or two with us, here are some guidelines to follow to ensure a standard
development procedure is followed.

1. Ensure you have the following tools already installed on your system:
   - [Python](https://www.python.org)
   - [Cookiecutter](https://cookiecutter.readthedocs.io)
   - [Pre-commit](https://pre-commit.com)
2. With the aforementioned tools installed and verified, clone the remote
   repository locally to your development environment by running the following
   command;

   ```console
   git clone git@github.com:Weburz/project-starters
   ```

3. Change directory in to the `project-starters` folder and then make your
   changes to the template files and/or create a new template for future usage.
4. Read the `cookiecutter` documentations to learn more about
   writing/maintaining the templates.

## Distribution Rights

This repository is expected to be used by `cookiecutter` to generate basic
project structures for all client work at Weburz. Hence, the license to use
`cookiecutter` is available for further reference in their
[official repository](https://github.com/cookiecutter/cookiecutter). But the
contents of this template repository are licensed under the MIT License. So, you
are free to use the contents of the repository as you wish as long as you adhere
to the terms and conditions detailed in the [LICENSE](./LICENSE) document.
