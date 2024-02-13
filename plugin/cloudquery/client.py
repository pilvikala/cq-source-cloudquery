from typing import Generator, Dict, Any
import requests

class CloudQueryClient:
    def __init__(self, base_url="https://api.example.com"):
        self._base_url = base_url

    def make_request(self, path: str, body: dict = {}):
        result = requests.get(f'{self._base_url}{path}', headers={
            "Content-Type": "application/json",
            })
        return result.json()["items"]

    def item_iterator(self, page: int = 1) -> Generator[Dict[str, Any], None, None]:
        plugin_data = self.make_request(f"/plugins?page={page}&per_page=1000")
        for p in plugin_data:
            yield p
