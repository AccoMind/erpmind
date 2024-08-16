from django.urls import path

from customer.views import CustomerAPIView, CustomerDetailAPIView

urlpatterns = [
    path('', CustomerAPIView.as_view(), name='customer'),
    path('<int:id>', CustomerDetailAPIView.as_view(), name='customer_detail'),
]