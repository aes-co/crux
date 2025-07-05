from pathlib import Path

def get_file_size(path: str | Path) -> int:
    return Path(path).stat().st_size

def get_human_size(size: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} PB"

def read_file(path: str | Path, encoding='utf-8') -> str:
    return Path(path).read_text(encoding=encoding)

def write_file(path: str | Path, content: str, encoding='utf-8'):
    Path(path).write_text(content, encoding=encoding)
