<h1 align="center">
  <img src="https://github.com/aes-co/crux/raw/main/.assets/logo.png" height="100"/>
  <br/>
  <b>Crux - Core Utility Library</b>
</h1>

<p align="center">
  A modular, lightweight Python utility toolkit designed for Telegram automation & projects by aes-co.
</p>

<p align="center">
  <a href="https://pypi.org/project/crux-aes/"><img src="https://img.shields.io/pypi/v/crux-aes?style=flat-square"/></a>
  <img src="https://img.shields.io/pypi/pyversions/crux-aes?style=flat-square"/>
  <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/status-stable-green?style=flat-square"/>
</p>

---

## ✨ Features

- ✅ `.env` and environment loader
-  Async HTTP fetch + downloader
-  Filesystem helpers (read/write/size)
-  Custom logger (no dependency)
-  Basic i18n support with fallback
-  Type-safe: enums & dataclasses
-  Utility helpers (time, plural, escape)

---

## Installation

```bash
pip install crux-aes
```

---

## Usage Example

```python
from crux import core, net, files, utils

core.load_dotenv()
print(core.get_mode())

# html = await net.async_fetch("https://example.com") # Uncomment and run in async context
# print(html[:100])

# print(files.get_human_size(files.get_file_size("somefile.txt"))) # Uncomment and provide a file
print(utils.format_time(135))
```

---

## Modules

| Module  | Description                                  |
| ------- | -------------------------------------------- |
| `core`  | ENV loader, mode getter, project root finder |
| `net`   | aiohttp async fetch/download                 |
| `files` | File read/write, size formatter              |
| `log`   | Colored lightweight logger                   |
| `lang`  | Simple i18n with fallback                    |
| `types` | Enum & dataclass types                       |
| `utils` | Time formatter, pluralizer, escaper          |
| `cli`   | (Optional) command-line interface            |

---

## License

This project is licensed under the [MIT License](./LICENSE).

---

## ❤️ About

Made with care by [@aesneverhere](https://github.com/aesneverhere) · Part of [aes-co](https://github.com/aes-co)