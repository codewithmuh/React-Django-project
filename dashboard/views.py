from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import  HttpResponse


from bigcommerce.api import BigcommerceApi
from decouple import config, Csv


def client_secret():
    return config('appClientSecret')

@xframe_options_exempt
def dashBoard(request):
    # if request.GET.get('signed_payload'):
    if request.GET.get('code') and request.GET.get('context') and request.GET.get('scope'):
        signed_payload = request.GET.get('signed_payload')
        BigcommerceApi.oauth_verify_payload(signed_payload, client_secret())
        return render(request ,'index.html')
        
    return HttpResponse('Some thing Went Wrong')
    
