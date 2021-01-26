from django.shortcuts import render
from .models import Modules
from django.http import HttpResponse
from django.core import serializers

# Create your views here.

"""modules = Modules.objects.all()
        modules_names_price = [module.nom + " : " + str(module.prix) + " €"
        for module in modules]
        modules_names__price_str = ", ".join(modules_names_price)
        return HtptpResponse("Les modules : " + modules_names__price_str)"""


def index(request):
    modules = Modules.objects.all().order_by('prix')
    return render(request, 'menu/index.html', {'module': modules})

def api_get_modules(request):
        modules = Modules.objects.all().order_by('prix')
        json = serializers.serialize("json", modules)
        return HttpResponse (json)
