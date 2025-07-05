class Logger:
    _COLOR_MAP = {
        'INFO': '\033[94m',  # Blue
        'WARN': '\033[93m',  # Yellow
        'ERROR': '\033[91m', # Red
        'RESET': '\033[0m'
    }

    def _log(self, level: str, message: str):
        color = self._COLOR_MAP.get(level, self._COLOR_MAP['RESET'])
        print(f"{color}{level}: {message}{self._COLOR_MAP['RESET']}")

    def info(self, message: str):
        self._log('INFO', message)

    def warn(self, message: str):
        self._log('WARN', message)

    def error(self, message: str):
        self._log('ERROR', message)

log = Logger()
