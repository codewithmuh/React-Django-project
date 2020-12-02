from django.shortcuts import render
from django.http import  HttpResponse
import requests
import datetime

from bigcommerce.api import BigcommerceApi
from decouple import config, Csv
from callback.models import Auth


def client_secret():
    return config('appClientSecret')

def client_id():
    return config('appClientId')





def auth(request):

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


        b = Auth.objects.create(mail = "dd@gmail.com", storehash = store_hash, token = access_token)

        return render(request , 'auth.html', {'token' : access_token})

    return HttpResponse("Something Went Wrong")
    
 
