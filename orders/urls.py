from django.urls import path

from . import views

urlpatterns = [ 
    path("", views.index, name="index"),   
    path("add_to_cart", views.add_to_cart, name="add_to_cart"),
    path("empty_cart", views.empty_cart, name="empty_cart"),
    path("remove_cart_item/<int:id>", views.remove_cart_item, name="remove_cart_item"),
    path("preview_checkout", views.preview_checkout, name="preview_checkout"),
    path("process_order", views.process_order, name="process_order"),
    path("my_orders", views.my_orders, name="my_orders"),
]
