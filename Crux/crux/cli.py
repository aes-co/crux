import os
import sys
import subprocess
import argparse
from crux import core, log

def _color_text(text: str, color_code: int) -> str:
    return f"
[{color_code}m{text}
[0m"

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

def info_command(args):
    log.info(f"Crux Mode: {core.get_mode()}")
    log.info(f"Project Root: {core.get_project_root()}")

def env_command(args):
    log.info("Loaded Environment Variables:")
    if not os.environ:
        log.info("  (No environment variables loaded)")
    for key, value in os.environ.items():
        log.info(f"  {key}={value}")

def test_command(args):
    log.info("Running Crux unit tests...")
    try:
        # Ensure pytest and pytest-cov are installed
        subprocess.run([sys.executable, "-m", "pip", "install", "pytest", "pytest-cov"], check=True, capture_output=True)
        
        # Run pytest with coverage
        result = subprocess.run(
            [sys.executable, "-m", "pytest", str(core.get_project_root() / "tests"), "--cov=crux"],
            capture_output=True, text=True, check=True
        )
        log.info(green("All tests passed!"))
        log.info("\n" + result.stdout)
    except subprocess.CalledProcessError as e:
        log.error(red("Tests failed!"))
        log.error("\n" + e.stdout)
        log.error("\n" + e.stderr)
        sys.exit(1)
    except Exception as e:
        log.error(red(f"An error occurred during testing: {e}"))
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Crux CLI for managing project utilities.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Info command
    info_parser = subparsers.add_parser("info", help="Prints basic info about the Crux environment.")
    info_parser.set_defaults(func=info_command)

    # Env command
    env_parser = subparsers.add_parser("env", help="Prints all loaded environment variables.")
    env_parser.set_defaults(func=env_command)

    # Test command
    test_parser = subparsers.add_parser("test", help="Runs internal unit tests with coverage.")
    test_parser.set_defaults(func=test_command)

    args = parser.parse_args()

    if args.command:
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
