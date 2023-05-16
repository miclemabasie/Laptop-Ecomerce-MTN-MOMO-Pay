from django.urls import path
from .views import laptop_list, laptop_detail, checkout, payment_pending, payment_failed

urlpatterns = [
    path("", laptop_list, name="laptop-list"),
    path("laptop/<int:pk>/", laptop_detail, name="laptop-detail"),
    path("checkout/", checkout, name="checkout"),
    path("payment-pending/", payment_pending, name="payment-pending"),
    path("payment-failed/", payment_failed, name="payment-failed"),
]
