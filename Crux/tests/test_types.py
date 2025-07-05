import unittest
from crux import types

class TestTypes(unittest.TestCase):

    def test_log_level_enum(self):
        self.assertEqual(types.LogLevel.INFO.value, "INFO")
        self.assertEqual(types.LogLevel.WARN.value, "WARN")
        self.assertEqual(types.LogLevel.ERROR.value, "ERROR")

    def test_bot_mode_enum(self):
        self.assertEqual(types.BotMode.DEV.value, "dev")
        self.assertEqual(types.BotMode.PROD.value, "prod")
        self.assertEqual(types.BotMode.DEBUG.value, "debug")

    def test_user_meta_dataclass(self):
        user1 = types.UserMeta(user_id=1, username="testuser", first_name="Test")
        self.assertEqual(user1.user_id, 1)
        self.assertEqual(user1.username, "testuser")
        self.assertEqual(user1.first_name, "Test")
        self.assertIsNone(user1.last_name)

        user2 = types.UserMeta(user_id=2, username="another", first_name="Another", last_name="User")
        self.assertEqual(user2.last_name, "User")
