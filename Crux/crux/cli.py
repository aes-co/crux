import os
import sys
import subprocess
from crux import core, log

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

def info_command():
    log.info(f"Crux Mode: {core.get_mode()}")
    log.info(f"Project Root: {core.get_project_root()}")

def env_command():
    log.info("Loaded Environment Variables:")
    for key, value in os.environ.items():
        log.info(f"  {key}={value}")

def test_command():
    log.info("Running Crux unit tests...")
    try:
        # Assuming pytest is installed in the environment
        subprocess.run([sys.executable, "-m", "pytest", str(core.get_project_root() / "tests")], check=True)
        log.info(green("All tests passed!"))
    except subprocess.CalledProcessError:
        log.error(red("Tests failed!"))
        sys.exit(1)

def main():
    if len(sys.argv) < 2:
        log.info("Usage: python -m crux.cli <command>")
        log.info("Commands: info, env, test")
        sys.exit(1)

    command = sys.argv[1]

    if command == "info":
        info_command()
    elif command == "env":
        env_command()
    elif command == "test":
        test_command()
    else:
        log.error(red(f"Unknown command: {command}"))
        sys.exit(1)

if __name__ == "__main__":
    main()