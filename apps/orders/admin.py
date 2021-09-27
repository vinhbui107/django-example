from django.contrib import admin

from apps.orders.models import Order, OrderItem


@admin.action(description="Update order status to Completed")
def update_status_completed(modeladmin, request, queryset):
    queryset.update(status=2)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 3


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["id", "buyer", "amount", "status", "notes"]
    search_fields = ["id", "buyer__username"]
    actions = [update_status_completed]

    ordering = ["id"]
    list_filter = ("status",)

    fieldsets = (
        ("Order's info", {"fields": ("buyer", "amount", "status")}),
        ("Important dates", {"fields": ("modified_at", "created_at")}),
    )

    inlines = [OrderItemInline]

    readonly_fields = ["buyer", "amount", "modified_at", "created_at"]
