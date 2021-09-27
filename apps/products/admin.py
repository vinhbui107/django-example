from django.contrib import admin
from django.db.models import Count, Q
from django.db.models.aggregates import Sum

from apps.products.models import Product
from apps.orders.models import Order


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "price",
        "stock",
        "is_active",
        "notes",
    )
    search_fields = ("name",)

    ordering = ("id",)
    list_filter = ("is_active",)

    readonly_fields = ["modified_at", "created_at"]
