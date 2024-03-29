from django.shortcuts import render
from django.http import  HttpResponse
from .models import Auth
import requests
import datetime

from bigcommerce.api import BigcommerceApi
from decouple import config, Csv
# from callback.models import Auth


def client_secret():
    return config('appClientSecret')

def client_id():
    return config('appClientId')




#function to check Callback
def auth(request):

    if request.GET.get('code') and request.GET.get('context') and request.GET.get('scope'):
        code = request.GET.get('code')
        context = request.GET.get('context')
        scope = request.GET.get('scope')

        # redirect = 'https://dd6100868f41.ngrok.io/auth'
        redirect = config('callBackURL')


        store_hash = context.split('/')[1]

        client = BigcommerceApi(client_id=client_id(), store_hash=store_hash)

        token = client.oauth_fetch_token(client_secret(), code, context, scope, redirect)
        bc_user_id = token['user']['id']
        email = token['user']['email']
        access_token = token['access_token']

        a , created = Auth.objects.get_or_create(storehash = store_hash)
        a.user_id = bc_user_id
        a.mail = email
        a.storehash = store_hash
        a.token = access_token
        a.save()

        return render(request , 'index.html')

    return HttpResponse("Something Went Wrong")
