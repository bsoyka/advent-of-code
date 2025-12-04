#!/usr/bin/env just --justfile

uv := require('uv')

@_default:
    just --list

# format code with Ruff
format:
    uv run ruff format

# set up pre-commit hooks
install-hooks:
    uv run pre-commit install

# lint and auto-fix code with Ruff
lint:
    uv run ruff check --fix

# run both linting and formatting with Ruff
ruff: lint format
