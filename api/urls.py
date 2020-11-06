from django.urls import path
from api.views import apitest

urlpatterns = [
    path('v2/orders', apitest, name="orderapi"),
]
