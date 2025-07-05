# Crux: The Core Engine for aes-co Projects

Crux is a lightweight, modular Python library serving as the foundational core engine for all projects within the aes-co ecosystem. It consolidates common utilities, ensuring code reusability, consistency, and adherence to a clean, minimalist design philosophy across all our bots and tools.

## Philosophy

Crux is built with the following principles:

-   **Minimalist & Modular**: Each module and function is focused on a single responsibility, promoting clarity and maintainability.
-   **Clean & Beautiful**: Emphasizes clear naming, logical structure, and elegant code without unnecessary complexity or comments.
-   **Reusable**: Designed to be easily integrated and used across diverse projects, from userbots to Telegram bots.
-   **No Hard Dependencies**: Relies primarily on pure Python, with external libraries used only when absolutely necessary (e.g., `aiohttp` for async networking).
-   **Lightweight & Fast**: Optimized for performance and minimal resource consumption, suitable for deployment on small VPS instances or Termux environments.

## Modules

Crux provides the following core modules:

-   `crux.core`: Environment and configuration handlers (`get_env`, `get_mode`, `get_project_root`, `load_dotenv`).
-   `crux.files`: File system utilities (`get_file_size`, `get_human_size`, `read_file`, `write_file`).
-   `crux.lang`: Lightweight multi-language support with fallback mechanisms (`Lang` class).
-   `crux.log`: Custom, minimalist colored logger for clean console output.
-   `crux.net`: Asynchronous networking utilities (`async_fetch`, `download_file`) using `aiohttp`.
-   `crux.types`: Shared enums and dataclasses (`LogLevel`, `BotMode`, `UserMeta`).
-   `crux.utils`: General utility functions (e.g., `format_time`, `escape`, `pluralize`).

## Installation

Crux is designed to be installed via pip:

```bash
pip install crux-aes
```

## Usage Examples

### Core Module

```python
from crux import core

core.load_dotenv()
mode = core.get_mode()
root_path = core.get_project_root()
env_var = core.get_env("MY_ENV_VAR", "default_value")

print(f"Running in {mode} mode from {root_path}")
print(f"MY_ENV_VAR: {env_var}")
```

### Log Module

```python
from crux import log

log.info("This is an informational message.")
log.warn("This is a warning message.")
log.error("This is an error message.")
```

### Net Module

```python
import asyncio
from crux import net

async def fetch_data():
    data = await net.async_fetch("https://api.github.com/users/aes-co")
    print(data)

async def download_example():
    await net.download_file("https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png", "google_logo.png")
    print("Google logo downloaded.")

# asyncio.run(fetch_data())
# asyncio.run(download_example())
```

### Lang Module

```python
from crux import lang

my_lang = lang.Lang(default_lang="en")
# Assuming you have a 'en.json' and 'id.json' in your project root
# my_lang.load_from_json("en", "en.json")
# my_lang.load_from_json("id", "id.json")

# print(my_lang.get("welcome_message", username="Alice"))
# print(my_lang.get("greeting", lang_code="id"))
```

### Files Module

```python
from crux import files

# files.write_file("test.txt", "Hello, Crux!")
# content = files.read_file("test.txt")
# size = files.get_file_size("test.txt")
# human_size = files.get_human_size(size)

# print(f"File content: {content}")
# print(f"File size: {human_size}")
```

### Types Module

```python
from crux import types

mode = types.BotMode.PROD
log_level = types.LogLevel.INFO
user = types.UserMeta(user_id=123, username="testuser", first_name="Test")

print(f"Bot Mode: {mode.value}")
print(f"Log Level: {log_level.value}")
print(f"User: {user.username}")
```

### Utils Module

```python
from crux import utils

time_str = utils.format_time(3723) # 01:02:03
plural_str = utils.pluralize(1, "item")
plural_str_2 = utils.pluralize(5, "item")
escaped_text = utils.escape("Hello *world*! [link](url)")

print(f"Formatted time: {time_str}")
print(f"Plural: {plural_str}")
print(f"Plural 2: {plural_str_2}")
print(f"Escaped text: {escaped_text}")
```

## Contributing

Contributions are welcome! Please refer to the `CONTRIBUTING.md` for guidelines.
