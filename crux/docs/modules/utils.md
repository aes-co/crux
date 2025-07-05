# Utilities Module

The `crux.utils` module provides a collection of general-purpose utility functions that are frequently needed across various projects.

## Functions

- `format_time(seconds: int) -> str`: Formats a duration in seconds into a human-readable string (e.g., "01:42:19" or "02:15").
- `escape(text: str) -> str`: Performs basic escaping for common Markdown/HTML special characters in a string.
- `pluralize(count: int, singular: str, plural: str = None) -> str`: Returns a string with the correct singular or plural form of a word based on the given count (e.g., "1 apple", "2 apples", "2 people").