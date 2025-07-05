def _color_text(text: str, color_code: int) -> str:
    return f"\033[{color_code}m{text}\033[0m"

def red(text: str) -> str:
    return _color_text(text, 31)

def green(text: str) -> str:
    return _color_text(text, 32)

def yellow(text: str) -> str:
    return _color_text(text, 33)

def blue(text: str) -> str:
    return _color_text(text, 34)

def magenta(text: str) -> str:
    return _color_text(text, 35)

def cyan(text: str) -> str:
    return _color_text(text, 36)

def white(text: str) -> str:
    return _color_text(text, 37)

def bold(text: str) -> str:
    return _color_text(text, 1)

def underline(text: str) -> str:
    return _color_text(text, 4)
