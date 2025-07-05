# Language Module

The `crux.lang` module offers a simple and lightweight solution for multi-language support (i18n) with built-in fallback mechanisms.

## Class: `Lang`

- `__init__(self, default_lang='en')`: Initializes the Lang instance with a default language.
- `load_from_json(self, lang_code: str, file_path: str)`: Loads translations for a specific language from a JSON file.
- `get(self, key: str, lang_code: str = None, **kwargs)`: Retrieves a translated string for a given key. It first tries the specified `lang_code`, then falls back to the `default_lang`, and finally returns the `key` itself if no translation is found. Supports dynamic string substitution using keyword arguments (e.g., `get("welcome", name="Alice")`).