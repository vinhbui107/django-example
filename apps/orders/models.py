from django.db import models

from apps.users.models import User
from apps.products.models import Product


ORDER_STATUS = (
    ("0", "Awaiting Payment"),
    ("1", "Shipped"),
    ("2", "Completed"),
    ("3", "Cancelled"),
    ("4", "Refunded"),
)


class Order(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")

    amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    status = models.CharField(max_length=1, choices=ORDER_STATUS, default=0)
    address = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "order"
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="orderitems"
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="orderitems"
    )

    quantity = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "order_item"
        verbose_name = "OrderItem"
        verbose_name_plural = "Order Items"
        unique_together = (
            "product",
            "order",
        )

    def __str__(self):
        return self.product.name
