"""HTTP entry point for placing orders."""

from services.order_service import OrderService


def create_order(order_id: str, customer_id: str, product_id: str) -> None:
    service = OrderService()
    service.place_order(order_id, customer_id, product_id)


if __name__ == "__main__":
    create_order("ord-1001", "cust-42", "sku-7")
