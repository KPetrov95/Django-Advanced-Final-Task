from django.urls import path

from bookStore.orders.views import CheckoutView, OrderListView, OrderDetailsView

urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('all/', OrderListView.as_view(), name='order_list'),
    path('<int:pk>/details/', OrderDetailsView.as_view(), name='order_details')
]