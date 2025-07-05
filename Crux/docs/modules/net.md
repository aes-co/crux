# Networking Module

The `crux.net` module offers asynchronous utilities for making HTTP requests and downloading files, built upon `aiohttp`.

## Functions

- `async_fetch(url: str)`: Performs an asynchronous GET request to the given URL. It automatically parses the response as JSON if the `Content-Type` is `application/json`, otherwise returns the response as plain text. Raises an `aiohttp.ClientResponseError` for unsuccessful responses.
- `download_file(url: str, destination_path: str)`: Asynchronously downloads a file from the given URL and saves it to the specified `destination_path`. Raises an `aiohttp.ClientResponseError` for unsuccessful responses.