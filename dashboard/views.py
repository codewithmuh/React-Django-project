from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt



@xframe_options_exempt
def home(request):
    template = "index.html"
    context = {}

    return render(request, template, context)
