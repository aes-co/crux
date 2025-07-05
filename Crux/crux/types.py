from enum import Enum
from dataclasses import dataclass

class LogLevel(Enum):
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"

class BotMode(Enum):
    DEV = "dev"
    PROD = "prod"
    DEBUG = "debug"

@dataclass
class UserMeta:
    user_id: int
    username: str
    first_name: str
    last_name: str = None
