from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
import json
from django.http import JsonResponse

from .models import Addresses


def index(request):
    return render(request, 'index.html')


def addresses(request):
    data = list(Addresses.objects.values())  # use list(), because QuerySet is not JSON serializable
    return JsonResponse(data, safe=False)
    # data = json.dumps(list(Addresses.objects.all().values('address')))


def multiroute(request):
    data = list(Addresses.objects.values())
    return render(request, 'multiroute.html', {"data": data})


def delivered(request, address_id):
    address = Addresses.objects.get(pk=address_id)
    address.delivered = True
    address.save()
    return render(request, 'multiroute.html')