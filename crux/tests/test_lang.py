import unittest
import json
from pathlib import Path
from crux import lang

class TestLang(unittest.TestCase):

    def setUp(self):
        self.lang_instance = lang.Lang(default_lang="en")
        self.en_json_path = Path("en.json")
        self.id_json_path = Path("id.json")

        with open(self.en_json_path, 'w') as f:
            json.dump({"hello": "Hello", "welcome": "Welcome, {name}!"}, f)
        with open(self.id_json_path, 'w') as f:
            json.dump({"hello": "Halo", "goodbye": "Sampai jumpa!"}, f)

    def tearDown(self):
        if self.en_json_path.exists():
            self.en_json_path.unlink()
        if self.id_json_path.exists():
            self.id_json_path.unlink()

    def test_load_from_json(self):
        self.lang_instance.load_from_json("en", self.en_json_path)
        self.assertIn("en", self.lang_instance.translations)
        self.assertEqual(self.lang_instance.translations["en"]["hello"], "Hello")

    def test_get_default_lang(self):
        self.lang_instance.load_from_json("en", self.en_json_path)
        self.assertEqual(self.lang_instance.get("hello"), "Hello")

    def test_get_specific_lang(self):
        self.lang_instance.load_from_json("en", self.en_json_path)
        self.lang_instance.load_from_json("id", self.id_json_path)
        self.assertEqual(self.lang_instance.get("hello", lang_code="id"), "Halo")

    def test_get_with_fallback(self):
        self.lang_instance.load_from_json("en", self.en_json_path)
        self.lang_instance.load_from_json("id", self.id_json_path)
        self.assertEqual(self.lang_instance.get("goodbye", lang_code="id"), "Sampai jumpa!")
        # Fallback to default (en) if not found in specific lang (id)
        self.assertEqual(self.lang_instance.get("welcome", lang_code="id", name="User"), "Welcome, User!")

    def test_get_with_kwargs(self):
        self.lang_instance.load_from_json("en", self.en_json_path)
        self.assertEqual(self.lang_instance.get("welcome", name="Alice"), "Welcome, Alice!")

    def test_get_key_not_found(self):
        self.lang_instance.load_from_json("en", self.en_json_path)
        self.assertEqual(self.lang_instance.get("non_existent_key"), "non_existent_key")
