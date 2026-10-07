"""Application configuration loaded at startup."""

import os

DATABASE_URL = os.environ["DATABASE_URL"]
CATALOG_BASE_URL = os.environ.get("CATALOG_BASE_URL", "https://catalog.internal/api")
PAYMENT_BASE_URL = os.environ.get("PAYMENT_BASE_URL", "https://payments.internal/v1")
REDIS_URL = os.environ.get("REDIS_URL", "redis://cache.internal:6379/0")
NOTIFICATIONS_QUEUE = os.environ.get("NOTIFICATIONS_QUEUE", "order-notifications")
