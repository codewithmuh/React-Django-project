from django.http import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from decouple import config, Csv
from callback.models import Auth
from django.shortcuts import get_object_or_404
from bigcommerce.api import BigcommerceApi

import url64
import json



def authHeader(request , signed_payload):
    print('lorem lorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsumlorem ipsum ipsum')
    print(signed_payload)
    # signed_payload='eyJ1c2VyIjp7ImlkIjoxODIyOTg1LCJlbWFpbCI6InJhc2hpZGRhaGE4MEBnbWFpbC5jb20ifSwib3duZXIiOnsiaWQiOjE4MjI5ODUsImVtYWlsIjoicmFzaGlkZGFoYTgwQGdtYWlsLmNvbSJ9LCJjb250ZXh0Ijoic3RvcmVzLzR6anV0YWlyaTgiLCJzdG9yZV9oYXNoIjoiNHpqdXRhaXJpOCIsInRpbWVzdGFtcCI6MTYxMDE4NDIyOS4yNDI5MzJ9.MzZlZWQ2MjQxMWVmYWFjMWE4ZDVkN2NiZmVkNzZkZGRjY2ZkZWU5MTMwMDMxZjM0ZmIyZTY5NTQyZTgyNDM0Zg%3D%3D'

    x = signed_payload.split(".")

    decoded = url64.decode(x[0])


    json_object = json.loads(decoded)
    __store_hash =json_object["store_hash"]






    authData = get_object_or_404(Auth, storehash = __store_hash)
    token = authData.token
    headers = {'X-Auth-Token':  token , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
    return __store_hash , headers



# Function to GET BigComerce Orders 
def orders(request):
     if request.GET.get('signed_payload'):
        signed_payload = request.GET.get('signed_payload')
        __store_hash , headers = authHeader(request, signed_payload)
        url = 'https://api.bigcommerce.com/stores/' + __store_hash + '/v2/orders'
        r = requests.get(url, headers=headers)
        return HttpResponse(r)

# Function to Update/Delete BigComerce Order 
@csrf_exempt
def order(request, id):
     if request.GET.get('signed_payload'):
        signed_payload = request.GET.get('signed_payload')
        __store_hash , headers = authHeader(request , signed_payload)
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
     if request.GET.get('signed_payload'):
        signed_payload = request.GET.get('signed_payload')
        __store_hash , headers = authHeader(request, signed_payload)
        url = 'https://api.bigcommerce.com/stores/' + __store_hash + '/v3/catalog/summary'
        r = requests.get(url, headers=headers)
        return HttpResponse(r)


# Function to Update/Delete BigComerce Catalog Summary        
@csrf_exempt
def resource(request, id):
     if request.GET.get('signed_payload'):
        signed_payload = request.GET.get('signed_payload')
        __store_hash , headers = authHeader(request, signed_payload)
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
    print('request  requestrequestrequestrequestrequestrequestrequestrequestrequestrequestrequestrequestrequestrequestrequestrequestrequestrequestrequestrequestrequestrequestrequestrequestrequestrequestrequestrequest')
    print(request)
    if request.GET.get('signed_payload'):
        signed_payload = request.GET.get('signed_payload')
        __store_hash , headers = authHeader(request , signed_payload)
        url = 'https://api.bigcommerce.com/stores/' + __store_hash + '/v2/store'
        r = requests.get(url, headers=headers)
        return HttpResponse(r)


