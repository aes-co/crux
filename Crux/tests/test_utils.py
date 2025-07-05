import unittest
from crux import utils

class TestUtils(unittest.TestCase):

    def test_format_time(self):
        self.assertEqual(utils.format_time(0), "00:00")
        self.assertEqual(utils.format_time(59), "00:59")
        self.assertEqual(utils.format_time(60), "01:00")
        self.assertEqual(utils.format_time(3600), "01:00:00")
        self.assertEqual(utils.format_time(3661), "01:01:01")

    def test_escape(self):
        self.assertEqual(utils.escape("Hello *world*!"), "Hello \*world\*!\\")
        self.assertEqual(utils.escape("_[test]_("), "\\_\[test\]\\_\\(")

    def test_pluralize(self):
        self.assertEqual(utils.pluralize(1, "apple"), "1 apple")
        self.assertEqual(utils.pluralize(2, "apple"), "2 apples")
        self.assertEqual(utils.pluralize(2, "person", "people"), "2 people")

