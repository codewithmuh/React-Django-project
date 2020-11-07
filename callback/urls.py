from django.urls import path
from callback.views import auth
urlpatterns = [
    path('auth', auth, name="ordersapi"),


]
