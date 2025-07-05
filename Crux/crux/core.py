import os
from pathlib import Path

def load_dotenv(dotenv_path: Path = None):
    if dotenv_path is None:
        dotenv_path = get_project_root() / '.env'

    if dotenv_path.is_file():
        with open(dotenv_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    key, value = line.split('=', 1)
                    os.environ[key] = value

def get_env(key: str, default=None):
    return os.getenv(key, default)

def get_mode() -> str:
    return os.getenv('CRUX_MODE', 'prod')

def get_project_root() -> Path:
    return Path(__file__).parent.parent
