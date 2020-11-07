
from django.contrib import admin
from django.urls import path

from dashboard.views import home
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html')),
]
