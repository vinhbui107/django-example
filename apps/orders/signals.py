from django.db.models import F, signals
from django.db.models import Sum
from django.dispatch import receiver

from apps.orders.models import OrderItem


@receiver(signals.post_save, sender=OrderItem)
def update_order(sender, instance, created, *args, **kwargs):
    order = instance.order

    new_amount = (
        OrderItem.objects.all()
        .select_related("product")
        .select_related("order")
        .filter(order=order)
        .aggregate(amount=Sum(F("quantity") * F("product__price")))
    )

    order.amount = new_amount["amount"]
    order.save()
