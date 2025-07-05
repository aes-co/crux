import unittest
import os
from pathlib import Path
from crux import core

class TestCore(unittest.TestCase):

    def setUp(self):
        # Clean up any existing CRUX_MODE env var
        if 'CRUX_MODE' in os.environ:
            del os.environ['CRUX_MODE']
        # Create a dummy .env file for testing load_dotenv
        self.dummy_env_path = Path(__file__).parent.parent / '.env.test'
        with open(self.dummy_env_path, 'w') as f:
            f.write("TEST_VAR=test_value\n")
            f.write("ANOTHER_VAR=another_value\n")

    def tearDown(self):
        # Clean up dummy .env file
        if self.dummy_env_path.exists():
            self.dummy_env_path.unlink()
        # Clean up any env vars set during test
        if 'TEST_VAR' in os.environ:
            del os.environ['TEST_VAR']
        if 'ANOTHER_VAR' in os.environ:
            del os.environ['ANOTHER_VAR']

    def test_get_mode(self):
        self.assertEqual(core.get_mode(), 'prod')
        os.environ['CRUX_MODE'] = 'dev'
        self.assertEqual(core.get_mode(), 'dev')
        os.environ['CRUX_MODE'] = 'debug'
        self.assertEqual(core.get_mode(), 'debug')

    def test_get_project_root(self):
        # This test assumes the project root is the parent of the Crux directory
        expected_root = Path(__file__).parent.parent
        self.assertEqual(core.get_project_root(), expected_root)

    def test_get_env(self):
        os.environ['TEST_ENV_VAR'] = 'hello'
        self.assertEqual(core.get_env('TEST_ENV_VAR'), 'hello')
        self.assertEqual(core.get_env('NON_EXISTENT_VAR'), None)
        self.assertEqual(core.get_env('NON_EXISTENT_VAR', 'default'), 'default')
        del os.environ['TEST_ENV_VAR']

    def test_load_dotenv(self):
        core.load_dotenv(self.dummy_env_path)
        self.assertEqual(os.getenv('TEST_VAR'), 'test_value')
        self.assertEqual(os.getenv('ANOTHER_VAR'), 'another_value')

if __name__ == '__main__':
    unittest.main()
