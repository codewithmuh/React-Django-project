from django.urls import path
from api.views import orders, order, resources, resource, store

urlpatterns = [
    path('v2/orders/', orders, name="ordersapi"),
        
    path('v2/orders/<int:id>/', order, name="orderapi"),
    path('', resources, name="orderapi"),
    
    path('<int:id>/', resource, name="orderapi"),


    path('v2/store/', store, name="orderapi"),
    path('v3/catalog/summary/', resources, name="orderapi"),

]
