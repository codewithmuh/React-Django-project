from django.http import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
import requests
import json


def orders(request):
        
    url = 'https://api.bigcommerce.com/stores/98oth9b1j7/v2/orders'
    headers = {'X-Auth-Token': 'tg6jy3weorvvrq25xrdqg1im9vlkoo1' , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers)
    return HttpResponse(r)


@csrf_exempt
def order(request, id):
        
    if(request.method == "PUT"):
        url = 'https://api.bigcommerce.com/stores/98oth9b1j7/v2/orders/{}'.format(id)
        headers = {'X-Auth-Token': 'tg6jy3weorvvrq25xrdqg1im9vlkoo1' , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
        body = json.loads(request.body)
        r = requests.put(url, headers=headers , json =body)
        return HttpResponse(r.content)

    if(request.method == "DELETE"):
        url = 'https://api.bigcommerce.com/stores/98oth9b1j7/v2/orders/{}'.format(id)
        headers = {'X-Auth-Token': 'tg6jy3weorvvrq25xrdqg1im9vlkoo1' , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
        r = requests.delete(url, headers=headers )
        return HttpResponse(r)

    url = 'https://api.bigcommerce.com/stores/98oth9b1j7/v2/orders/{}'.format(id)
    headers = {'X-Auth-Token': 'tg6jy3weorvvrq25xrdqg1im9vlkoo1' , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers )
    return HttpResponse(r)

    


       
@csrf_exempt
def resources(request):

    url = 'https://api.bigcommerce.com/stores/98oth9b1j7/v3/catalog/summary'
    headers = {'X-Auth-Token': 'tg6jy3weorvvrq25xrdqg1im9vlkoo1' , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers)
    return HttpResponse(r)



@csrf_exempt
def resource(request, id):
    if(request.method == "PUT"):
        url = 'https://api.bigcommerce.com/stores/98oth9b1j7/v3/catalog/summary/{}'.format(id)
        headers = {'X-Auth-Token': 'tg6jy3weorvvrq25xrdqg1im9vlkoo1' , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
        body = json.loads(request.body)
        r = requests.put(url, headers=headers , json =body)
        return HttpResponse(r.content)

    if(request.method == "DELETE"):
        url = 'https://api.bigcommerce.com/stores/98oth9b1j7/v3/catalog/summary/{}'.format(id)
        headers = {'X-Auth-Token': 'tg6jy3weorvvrq25xrdqg1im9vlkoo1' , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
        body = json.loads(request.body)
        r = requests.delete(url, headers=headers , json =body)
        return HttpResponse(r.content)
    
    url = 'https://api.bigcommerce.com/stores/98oth9b1j7/v3/catalog/summary/{}'.format(id)
    headers = {'X-Auth-Token': 'tg6jy3weorvvrq25xrdqg1im9vlkoo1' , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json' }
    body = json.loads(request.body)
    r = requests.delete(url, headers=headers , json =body)
    return HttpResponse(r.content)





@csrf_exempt
def store(request):
    url = 'https://api.bigcommerce.com/stores/98oth9b1j7/v2/store'
    headers = {'X-Auth-Token': 'tg6jy3weorvvrq25xrdqg1im9vlkoo1' , 'Accept': 'application/json', 'host':'api.bigcommerce.com'  ,'Content-Type': 'application/json'}
    r = requests.get(url, headers=headers)
    return HttpResponse(r)


