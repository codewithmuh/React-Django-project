from django.shortcuts import render
from django.http import  HttpResponse
import requests
import datetime

from bigcommerce.api import BigcommerceApi


def client_secret():
    return config('appClientSecret')




def auth(request):
    print(request.path_info)

    if request.GET.get('code') and request.GET.get('context') and request.GET.get('scope'):
        code = request.GET.get('code')
        context = request.GET.get('context')
        scope = request.GET.get('scope')
        redirect = 'https://bigcommerceapptest.herokuapp.com/cb/auth'
        
        store_hash = context.split('/')[1]

        client = BigcommerceApi(client_id=config('appClientId') , store_hash=config('apiStoreHash'))
        token = client.oauth_fetch_token(client_secret(), code, context, scope, redirect)
        bc_user_id = token['user']['id']
        email = token['user']['email']
        access_token = token['access_token']

        response = HttpResponse("App is Installed Successfully")
        return response
    
    return HttpResponse("Something Went Wrong")
