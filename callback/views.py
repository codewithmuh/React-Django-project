from django.shortcuts import render
from django.http import  HttpResponse
import requests


def auth(request):
    print(request.path_info)
    return HttpResponse('Auth Test')