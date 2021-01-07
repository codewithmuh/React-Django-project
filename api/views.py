from django.http import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from decouple import config, Csv
from callback.models import Auth
from django.shortcuts import get_object_or_404
from bigcommerce.api import BigcommerceApi
import datetime



def client_secret():
    return config('appClientSecret')

def authKey(request):
    signed_payload = request.GET.get('signed_payload')
    a = BigcommerceApi.oauth_verify_payload(signed_payload, client_secret())
    store_hash = a['store_hash']
    obj = get_object_or_404(Auth, storehash=store_hash)
    token = obj.token
    print(token)







# Function to GET BigComerce Orders 
def orders(request):

    signed_payload = request.GET.get('signed_payload')
    a = BigcommerceApi.oauth_verify_payload(signed_payload, client_secret())
    # store_hash = a['store_hash']
    # obj = get_object_or_404(Auth, storehash=store_hash)
    # token = obj.token
    print(a)

    url = 'https://api.bigcommerce.com/stores/' + config('apiStoreHash') + '/v2/orders'
    headers = {'X-Auth-Token':  config('apiToken') , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers)
    return HttpResponse(r)

# Function to Update/Delete BigComerce Order 
@csrf_exempt
def order(request, id):
        
    if(request.method == "PUT"):

        url = 'https://api.bigcommerce.com/stores/' + config('apiStoreHash') + '/v2/orders/{}'.format(id)
        headers = {'X-Auth-Token':  config('apiToken') , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
        body = json.loads(request.body)
        r = requests.put(url, headers=headers , json =body)
        return HttpResponse(r.content)

    if(request.method == "DELETE"):
        url = 'https://api.bigcommerce.com/stores/' + config('apiStoreHash') + '/v2/orders/{}'.format(id)
        headers = {'X-Auth-Token':  config('apiToken') , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
        r = requests.delete(url, headers=headers )
        return HttpResponse(r)

    url = 'https://api.bigcommerce.com/stores/' + config('apiStoreHash') + '/v2/orders/{}'.format(id)
    headers = {'X-Auth-Token':  config('apiToken') , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers )
    return HttpResponse(r)

    


# Function to GET BigComerce Catalog Summary        
@csrf_exempt
def resources(request):
    url = 'https://api.bigcommerce.com/stores/' + config('apiStoreHash') + '/v3/catalog/summary'
    headers = {'X-Auth-Token':  config('apiToken') , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers)
    return HttpResponse(r)


# Function to Update/Delete BigComerce Catalog Summary        
@csrf_exempt
def resource(request, id):
    if(request.method == "PUT"):
        url = 'https://api.bigcommerce.com/stores/' + config('apiStoreHash') + '/v3/catalog/summary/{}'.format(id)
        headers = {'X-Auth-Token':  config('apiToken') , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
        body = json.loads(request.body)
        r = requests.put(url, headers=headers , json =body)
        return HttpResponse(r.content)

    if(request.method == "DELETE"):
        url = 'https://api.bigcommerce.com/stores/' + config('apiStoreHash') + '/v3/catalog/summary/{}'.format(id)
        headers = {'X-Auth-Token':  config('apiToken') , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
        body = json.loads(request.body)
        r = requests.delete(url, headers=headers , json =body)
        return HttpResponse(r.content)
    
    url = 'https://api.bigcommerce.com/stores/' + config('apiStoreHash') + '/v3/catalog/summary/{}'.format(id)
    headers = {'X-Auth-Token':  config('apiToken') , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
    body = json.loads(request.body)
    r = requests.delete(url, headers=headers , json =body)
    return HttpResponse(r.content)




# Function to GET BigComerce Store
@csrf_exempt
def store(request):
    url = 'https://api.bigcommerce.com/stores/' + config('apiStoreHash') + '/v2/store'
    headers = {'X-Auth-Token': config('apiToken') , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers)
    return HttpResponse(r)


