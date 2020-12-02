from django.http import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json
from decouple import config, Csv



def getToken(request):
    if request.GET.get('code') and request.GET.get('context') and request.GET.get('scope'):
        code = request.GET.get('code')
        context = request.GET.get('context')
        scope = request.GET.get('scope')
        redirect = 'https://bigcommerce02.herokuapp.com/cb/auth'
        
        store_hash = context.split('/')[1]

        client = BigcommerceApi(client_id=client_id(), store_hash=config('apiStoreHash'))

        token = client.oauth_fetch_token(client_secret(), code, context, scope, redirect)
        bc_user_id = token['user']['id']
        email = token['user']['email']
        access_token = token['access_token']
        return access_token


def orders(request):

    access_token = getToken(request)
    print(access_token)
    url = 'https://api.bigcommerce.com/stores/4zjutairi8/v2/orders'
    headers = {'X-Auth-Token':  config('apiToken') , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers)
    return HttpResponse(r)


@csrf_exempt
def order(request, id):
        
    if(request.method == "PUT"):

        url = 'https://api.bigcommerce.com/stores/4zjutairi8/v2/orders/{}'.format(id)
        headers = {'X-Auth-Token':  config('apiToken') , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
        body = json.loads(request.body)
        r = requests.put(url, headers=headers , json =body)
        return HttpResponse(r.content)

    if(request.method == "DELETE"):
        url = 'https://api.bigcommerce.com/stores/4zjutairi8/v2/orders/{}'.format(id)
        headers = {'X-Auth-Token':  config('apiToken') , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
        r = requests.delete(url, headers=headers )
        return HttpResponse(r)

    url = 'https://api.bigcommerce.com/stores/4zjutairi8/v2/orders/{}'.format(id)
    headers = {'X-Auth-Token':  config('apiToken') , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers )
    return HttpResponse(r)

    


       
@csrf_exempt
def resources(request):
    url = 'https://api.bigcommerce.com/stores/4zjutairi8/v3/catalog/summary'
    headers = {'X-Auth-Token':  config('apiToken') , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers)
    return HttpResponse(r)



@csrf_exempt
def resource(request, id):
    if(request.method == "PUT"):
        url = 'https://api.bigcommerce.com/stores/4zjutairi8/v3/catalog/summary/{}'.format(id)
        headers = {'X-Auth-Token':  config('apiToken') , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
        body = json.loads(request.body)
        r = requests.put(url, headers=headers , json =body)
        return HttpResponse(r.content)

    if(request.method == "DELETE"):
        url = 'https://api.bigcommerce.com/stores/4zjutairi8/v3/catalog/summary/{}'.format(id)
        headers = {'X-Auth-Token':  config('apiToken') , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
        body = json.loads(request.body)
        r = requests.delete(url, headers=headers , json =body)
        return HttpResponse(r.content)
    
    url = 'https://api.bigcommerce.com/stores/4zjutairi8/v3/catalog/summary/{}'.format(id)
    headers = {'X-Auth-Token':  config('apiToken') , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
    body = json.loads(request.body)
    r = requests.delete(url, headers=headers , json =body)
    return HttpResponse(r.content)





@csrf_exempt
def store(request):
    url = 'https://api.bigcommerce.com/stores/4zjutairi8/v2/store'
    headers = {'X-Auth-Token': config('apiToken') , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers)
    return HttpResponse(r)


