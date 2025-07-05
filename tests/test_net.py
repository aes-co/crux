import unittest
from unittest.mock import AsyncMock, patch
import asyncio
from crux import net

class TestNet(unittest.IsolatedAsyncioTestCase):

    @patch('aiohttp.ClientSession.get')
    async def test_async_fetch_text(self, mock_get):
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.headers = {'Content-Type': 'text/plain'}
        mock_response.text.return_value = "Hello, world!"
        mock_get.return_value.__aenter__.return_value = mock_response

        result = await net.async_fetch("http://example.com")
        self.assertEqual(result, "Hello, world!")

    @patch('aiohttp.ClientSession.get')
    async def test_async_fetch_json(self, mock_get):
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.headers = {'Content-Type': 'application/json'}
        mock_response.json.return_value = {"key": "value"}
        mock_get.return_value.__aenter__.return_value = mock_response

        result = await net.async_fetch("http://example.com/api")
        self.assertEqual(result, {"key": "value"})

    @patch('aiohttp.ClientSession.get')
    async def test_download_file(self, mock_get):
        mock_response = AsyncMock()
        mock_response.status = 200
        mock_response.content.read.side_effect = [b"chunk1", b"chunk2", b""]
        mock_get.return_value.__aenter__.return_value = mock_response

        test_file_path = "test_download.txt"
        await net.download_file("http://example.com/file.txt", test_file_path)

        with open(test_file_path, 'rb') as f:
            content = f.read()
        self.assertEqual(content, b"chunk1chunk2")

        # Clean up the test file
        os.remove(test_file_path)

    @patch('aiohttp.ClientSession.get')
    async def test_async_fetch_error(self, mock_get):
        mock_response = AsyncMock()
        mock_response.status = 404
        mock_response.raise_for_status.side_effect = aiohttp.ClientResponseError(request_info=None, history=(), status=404)
        mock_get.return_value.__aenter__.return_value = mock_response

        with self.assertRaises(aiohttp.ClientResponseError):
            await net.async_fetch("http://example.com/nonexistent")
