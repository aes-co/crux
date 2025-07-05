# Usage Examples

This section provides basic usage examples for each module in Crux.

## Core Module

```python
from crux import core

core.load_dotenv()
mode = core.get_mode()
root_path = core.get_project_root()
env_var = core.get_env("MY_ENV_VAR", "default_value")

print(f"Running in {mode} mode from {root_path}")
print(f"MY_ENV_VAR: {env_var}")
```

## Log Module

```python
from crux import log

log.info("This is an informational message.")
log.warn("This is a warning message.")
log.error("This is an error message.")
```

## Net Module

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

## Lang Module

```python
from crux import lang

my_lang = lang.Lang(default_lang="en")
# Assuming you have a 'en.json' and 'id.json' in your project root
# my_lang.load_from_json("en", "en.json")
# my_lang.load_from_json("id", "id.json")

# print(my_lang.get("welcome_message", username="Alice"))
# print(my_lang.get("greeting", lang_code="id"))
```

## Files Module

```python
from crux import files

# files.write_file("test.txt", "Hello, Crux!")
# content = files.read_file("test.txt")
# size = files.get_file_size("test.txt")
# human_size = files.get_human_size(size)

# print(f"File content: {content}")
# print(f"File size: {human_size}")
```

## Types Module

```python
from crux import types

mode = types.BotMode.PROD
log_level = types.LogLevel.INFO
user = types.UserMeta(user_id=123, username="testuser", first_name="Test")

print(f"Bot Mode: {mode.value}")
print(f"Log Level: {log_level.value}")
print(f"User: {user.username}")
```

## Utils Module

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

## CLI Module

```bash
python -m crux.cli info
python -m crux.cli env
python -m crux.cli test
```