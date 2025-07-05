# Logging Module

The `crux.log` module provides a custom, lightweight, and colored logger for clean console output, designed to be used without external logging dependencies.

## Usage

Import the `log` instance directly:

```python
from crux import log

log.info("This is an informational message.")
log.warn("This is a warning message.")
log.error("This is an error message.")
```