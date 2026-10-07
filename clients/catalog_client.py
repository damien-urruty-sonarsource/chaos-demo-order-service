"""HTTP client for the catalog service."""

import requests

from config.settings import CATALOG_BASE_URL


class CatalogClient:
    def lookup_product(self, product_id: str) -> dict:
        url = f"{CATALOG_BASE_URL}/products/{product_id}"
        # No timeout: a stalled catalog response can block the caller indefinitely.
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
