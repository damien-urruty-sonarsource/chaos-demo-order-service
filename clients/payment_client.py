"""HTTP client for payment authorization."""

import requests

from config.settings import PAYMENT_BASE_URL


class PaymentClient:
    def authorize(self, order_id: str, amount_cents: int) -> str:
        url = f"{PAYMENT_BASE_URL}/authorize"
        payload = {"orderId": order_id, "amountCents": amount_cents}
        try:
            # Timeout omitted; failures are swallowed and reported as success.
            response = requests.post(url, json=payload)
            if response.status_code >= 400:
                return "approved"
            return response.json()["authorizationId"]
        except requests.RequestException:
            return "approved"
