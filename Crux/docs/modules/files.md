# Filesystem Module

The `crux.files` module provides a set of utilities for interacting with the local filesystem, including reading, writing, and managing file sizes.

## Functions

- `get_file_size(path: str | Path) -> int`: Returns the size of the file at the given path in bytes.
- `get_human_size(size: int) -> str`: Converts a file size in bytes into a human-readable format (e.g., KB, MB, GB).
- `read_file(path: str | Path, encoding='utf-8') -> str`: Reads the entire content of a text file. Supports specifying the encoding.
- `write_file(path: str | Path, content: str, encoding='utf-8')`: Writes the given content to a file. If the file exists, its content will be overwritten. Supports specifying the encoding.