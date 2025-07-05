# CLI Module

The `crux.cli` module provides a command-line interface for interacting with Crux utilities. It allows you to quickly get information about your environment, inspect loaded variables, and run tests.

## Usage

YouYou can run Crux CLI commands using `python -m crux.cli <command>`.

### `info` Command

Prints basic information about the Crux environment, including the operating mode, project root path, and Python version.

```bash
python -m crux.cli info
```

### `env` Command

Lists all environment variables that start with `CRUX_`.

```bash
python -m crux.cli env
```

### `test` Command

Runs the internal unit tests for Crux using `pytest` and `pytest-cov`. It will automatically install these dependencies if they are missing. The command also provides test coverage information.

```bash
python -m crux.cli test
```