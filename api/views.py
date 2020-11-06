from django.shortcuts import render
from django.http import JsonResponse
import json
import bigcommerce

api = bigcommerce.api.BigcommerceApi(client_id='5qtzag0m03gnh5c2ytrbliyhezmnk3g', store_hash='98oth9b1j7', access_token='tg6jy3weorvvrq25xrdqg1im9vlkoo1')

def apitest(request):
        
        BG_ORDER =[] 

        for obj in api.Orders.all():
            bg_order_obj ={}
            bg_order_obj['id'] = obj.id
            bg_order_obj['billing_address'] = obj.billing_address
            bg_order_obj['total_inc_tax'] = obj.total_inc_tax
            bg_order_obj['billing_address'] = obj.billing_address
            bg_order_obj['status'] = obj.status
            bg_order_obj['status_id'] = obj.status_id

            BG_ORDER.append(bg_order_obj)

        return JsonResponse(BG_ORDER , safe=False)

