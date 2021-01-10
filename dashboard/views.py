from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import  HttpResponse

from bigcommerce.api import BigcommerceApi
from decouple import config, Csv


def client_secret():
    return config('appClientSecret')

@xframe_options_exempt
def dashBoard(request):
    if request.GET.get('signed_payload'):
        signed_payload = request.GET.get('signed_payload')
        a = BigcommerceApi.oauth_verify_payload(signed_payload, client_secret())
        store_hash = a['store_hash']
        return render(request ,'index.html')
    return HttpResponse('Some thing Went Wrong')
