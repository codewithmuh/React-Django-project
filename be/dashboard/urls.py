from django.urls import path
from dashboard.views import home

urlpatterns = [
    path('', home, name="inccdex"),
]