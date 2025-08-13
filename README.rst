==================
Rompy Cookiecutter
==================

Cookiecutter_ template for a Rompy model config package.

Create a new Rompy model config package with all the necessary boilerplate.

.. _Cookiecutter: https://github.com/rom-py/cookiecutter-rompy

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Rompy model config package project::

    cookiecutter https://github.com/rom-py/cookiecutter-rompy.git


Code Formatting and Pre-commit Hooks
------------------------------------

This repository enforces Python code formatting using [black](https://github.com/psf/black) via the pre-commit framework.

To set up pre-commit hooks locally (required for all contributors)::

    pip install pre-commit
    pre-commit install

This will automatically check code formatting before each commit. To format your code manually, run::

    pre-commit run --all-files

All code must pass black formatting before it can be committed or merged.
