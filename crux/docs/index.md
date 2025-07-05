# Crux Documentation

Welcome to the official documentation for Crux, the core utility library for aes-co projects.

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
-   `crux.cli`: Command-line interface for Crux utilities.
-   `crux.ext`: Extensible plugin system.