# Core Module

The `crux.core` module provides essential functionalities for managing environment variables, determining the application's operating mode, and locating the project's root directory.

## Functions

- `load_dotenv(dotenv_path: Path = None)`: Loads environment variables from a `.env` file. If `dotenv_path` is not provided, it defaults to `.env` in the project root.
- `get_env(key: str, default=None)`: Retrieves the value of an environment variable. Returns `default` if the key is not found.
- `get_mode() -> str`: Returns the current operating mode ('prod', 'dev', or 'debug') based on the `CRUX_MODE` environment variable. Defaults to 'prod'.
- `get_project_root() -> Path`: Returns the absolute path to the project's root directory as a `pathlib.Path` object.