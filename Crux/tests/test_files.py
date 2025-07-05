import unittest
from pathlib import Path
from crux import files

class TestFiles(unittest.TestCase):

    def setUp(self):
        self.test_file = Path("test_file.txt")
        self.test_file.write_text("Hello, Crux!")

    def tearDown(self):
        if self.test_file.exists():
            self.test_file.unlink()

    def test_get_file_size(self):
        self.assertEqual(files.get_file_size(self.test_file), len("Hello, Crux!"))

    def test_get_human_size(self):
        self.assertEqual(files.get_human_size(1023), "1023.00 B")
        self.assertEqual(files.get_human_size(1024), "1.00 KB")
        self.assertEqual(files.get_human_size(1024 * 1024), "1.00 MB")

    def test_read_file(self):
        self.assertEqual(files.read_file(self.test_file), "Hello, Crux!")

    def test_write_file(self):
        new_content = "New content for the file."
        files.write_file(self.test_file, new_content)
        self.assertEqual(self.test_file.read_text(), new_content)
