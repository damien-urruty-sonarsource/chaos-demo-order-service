"""Coordinates checkout across catalog, payments, database, and notifications."""

from clients.catalog_client import CatalogClient
from clients.payment_client import PaymentClient
from repositories.order_repository import OrderRepository
from workers.notification_worker import NotificationWorker


class OrderService:
    def __init__(self) -> None:
        self._catalog = CatalogClient()
        self._payments = PaymentClient()
        self._orders = OrderRepository()
        self._notifications = NotificationWorker()

    def place_order(self, order_id: str, customer_id: str, product_id: str) -> None:
        product = self._catalog.lookup_product(product_id)
        total_cents = int(product["priceCents"])
        self._orders.save_order(order_id, customer_id, total_cents)
        authorization_id = self._payments.authorize(order_id, total_cents)
        if authorization_id:
            self._orders.mark_paid(order_id)
        self._notifications.publish_order_created(order_id, customer_id)
