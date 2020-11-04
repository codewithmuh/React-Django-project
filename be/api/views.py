from django.shortcuts import render
from django.http import JsonResponse
import json

from django.http import HttpResponse





# Create your views here.


import bigcommerce

# Public apps (OAuth)
# Access_token is optional, if you don't have one you can use oauth_fetch_token (see below)
api = bigcommerce.api.BigcommerceApi(client_id='5qtzag0m03gnh5c2ytrbliyhezmnk3g', store_hash='98oth9b1j7', access_token='tg6jy3weorvvrq25xrdqg1im9vlkoo1')

# Private apps (Basic Auth)
# api = bigcommerce.api.BigcommerceApi(host='store.mybigcommerce.com', basic_auth=('username', 'api token'))

def apitest(request):
        
        l_products =[] 

        for obj in api.Products.all():
            l_dictObj ={}
            l_dictObj['_id'] = obj.id
            l_dictObj['name'] = obj.name

            #...more fields here
            l_products.append(l_dictObj)

        # print(data)
        return JsonResponse(l_products , safe=False)
        # return HttpResponse(l_products)

