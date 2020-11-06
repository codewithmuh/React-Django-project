from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt


# import bigcommerce


# def home(request):
#     l_products = 'Hello'
#     return HttpResponse(l_products)


@xframe_options_exempt
def home(request):
    # api = bigcommerce.api.BigcommerceApi(client_id='5qtzag0m03gnh5c2ytrbliyhezmnk3g', store_hash='98oth9b1j7', access_token='tg6jy3weorvvrq25xrdqg1im9vlkoo1')
    # print(bigcommerce.oauth_verify_payload('signed_payload' ))
    template = "index.html"
    print(request)

    context = {
    }

    return render(request, template, context)
