from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.clickjacking import xframe_options_exempt


class home(TemplateView):
    @xframe_options_exempt
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
