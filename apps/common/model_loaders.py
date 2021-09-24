from django.apps import apps


def get_user_model():
    return apps.get_model("users", "User")


def get_product_model():
    return apps.get_model("products", "Product")


def get_order_model():
    return apps.get_model("orders", "Orders")


def get_order_item_model():
    return apps.get_model("orders", "OrderItem")
