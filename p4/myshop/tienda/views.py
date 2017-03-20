from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from tienda.models import Bike


def index(request):
    latest_bikes_list = Bike.objects.order_by('-pub_date')[:30]
    template = loader.get_template('tienda/index.html')
    context = {
        'latest_bikes_list': latest_bikes_list,
    }
    return HttpResponse(template.render(context, request))
