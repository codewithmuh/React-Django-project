from django.http import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from callback.models import Auth
from django.shortcuts import get_object_or_404
import url64
import json


@csrf_exempt
def authData(request ):

    payload = request.GET.get('payload')


    x = payload.split("=")
    y = x[1].split(".")
    decoded = url64.decode(y[0])
    json_object = json.loads(decoded)
    __store_hash =json_object["store_hash"]
    authData = get_object_or_404(Auth, storehash = __store_hash)
    token = authData.token
    headers = {'X-Auth-Token':  token , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
    return __store_hash , headers



# Function to GET BigComerce Orders 
def orders(request):
    __store_hash , headers = authData(request)
    url = 'https://api.bigcommerce.com/stores/' + __store_hash + '/v2/orders'
    r = requests.get(url, headers=headers)
    return HttpResponse(r)

# Function to Update/Delete BigComerce Order 
@csrf_exempt
def order(request, id):
    __store_hash , headers = authData(request)
    url = 'https://api.bigcommerce.com/stores/' + __store_hash + '/v2/orders/{}'.format(id)
    if(request.method == "PUT"):
        body = json.loads(request.body)
        r = requests.put(url, headers=headers , json =body)
        return HttpResponse(r.content)

    if(request.method == "DELETE"):
        r = requests.delete(url, headers=headers )
        return HttpResponse(r)


    r = requests.get(url, headers=headers )
    return HttpResponse(r)




# Function to GET BigComerce Catalog Summary        
@csrf_exempt
def resources(request):
    __store_hash , headers = authData(request)
    url = 'https://api.bigcommerce.com/stores/' + __store_hash + '/v3/catalog/summary'
    r = requests.get(url, headers=headers)
    return HttpResponse(r)


# Function to Update/Delete BigComerce Catalog Summary        
@csrf_exempt
def resource(request, id):
    __store_hash , headers = authData(request)
    url = 'https://api.bigcommerce.com/stores/' + __store_hash + '/v3/catalog/summary/{}'.format(id)
    body = json.loads(request.body)
    if(request.method == "PUT"):
        r = requests.put(url, headers=headers , json =body)
        return HttpResponse(r.content)

    if(request.method == "DELETE"):
        r = requests.delete(url, headers=headers , json =body)
        return HttpResponse(r.content)
    
    r = requests.delete(url, headers=headers , json =body)
    return HttpResponse(r.content)




# Function to GET BigComerce Store
@csrf_exempt
def store(request):
    __store_hash , headers = authData(request)
    url = 'https://api.bigcommerce.com/stores/' + __store_hash + '/v2/store'


    r = requests.get(url, headers=headers)
    return HttpResponse(r)


