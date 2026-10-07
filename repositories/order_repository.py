"""Persistence layer for orders."""

import psycopg2

from config.settings import DATABASE_URL


class OrderRepository:
    def __init__(self) -> None:
        # Connection acquisition has no connect_timeout or statement_timeout configured.
        self._connection = psycopg2.connect(DATABASE_URL)

    def save_order(self, order_id: str, customer_id: str, total_cents: int) -> None:
        query = (
            "INSERT INTO orders (id, customer_id, total_cents) "
            "VALUES (%s, %s, %s)"
        )
        with self._connection.cursor() as cursor:
            cursor.execute(query, (order_id, customer_id, total_cents))
        self._connection.commit()

    def mark_paid(self, order_id: str) -> None:
        query = "UPDATE orders SET status = 'PAID' WHERE id = %s"
        with self._connection.cursor() as cursor:
            cursor.execute(query, (order_id,))
        self._connection.commit()
