
from django.contrib import admin
from django.urls import path

from dashboard.views import dashBoard
from django.views.generic import TemplateView


urlpatterns = [

    path('', dashBoard, name="ordersapi"),

]
