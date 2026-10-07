"""Background worker that publishes order notifications."""

import json
import time

import redis

from config.settings import NOTIFICATIONS_QUEUE, REDIS_URL


class NotificationWorker:
    def __init__(self) -> None:
        self._redis = redis.Redis.from_url(REDIS_URL)

    def publish_order_created(self, order_id: str, customer_id: str) -> None:
        payload = json.dumps({"orderId": order_id, "customerId": customer_id})
        # Unbounded retry with no backoff can amplify outages on the queue service.
        while True:
            try:
                self._redis.lpush(NOTIFICATIONS_QUEUE, payload)
                return
            except redis.RedisError:
                time.sleep(0.01)
