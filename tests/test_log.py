import unittest
from unittest.mock import patch
import io
from crux import log

class TestLog(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_info_log(self, mock_stdout):
        log.log.info("Test info message")
        self.assertIn("INFO: Test info message", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_warn_log(self, mock_stdout):
        log.log.warn("Test warn message")
        self.assertIn("WARN: Test warn message", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_error_log(self, mock_stdout):
        log.log.error("Test error message")
        self.assertIn("ERROR: Test error message", mock_stdout.getvalue())
