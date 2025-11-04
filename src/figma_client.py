import os
import requests


class FigmaClient:
    """Simple client for interacting with the Figma REST API."""

    def __init__(self, figma_token: str):
        if not figma_token:
            raise ValueError("Figma access token is missing.")
        self.token = figma_token
        self.headers = {"X-Figma-Token": self.token}

    def get_file(self, file_key: str) -> dict:
        """Fetch the Figma file data for the given file key."""
        if not file_key:
            raise ValueError("File key is required.")

        url = f"https://api.figma.com/v1/files/{file_key}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()

        return response.json()
