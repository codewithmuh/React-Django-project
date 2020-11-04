from django.urls import path
from api.views import apitest

urlpatterns = [
    path('', apitest, name="inccdex"),
]