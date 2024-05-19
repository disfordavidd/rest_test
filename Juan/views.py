from django.shortcuts import render
from django.conf import settings
from .models import Lampara

import requests

# Create your views here.
def lamparas(request):
    if request.method == "GET":
        lamparas = Lampara.objects.all()
        return render(request, "lamparaslista.html", {
            "lamparas": lamparas
        })
    
    if request.method == "POST":
        if request.POST["_method"] == "DELETE":
            print("Eliminar elemento")
            """request.method = "DELETE"
            request.META['REQUEST_METHOD'] = 'DELETE'
            request.DELETE = QueryDict(request.body)"""
            #current_site = Site.objects.get_current()
            #current_site.domain
            res = requests.delete(settings.SITE_URL+request.POST["endpoint"])

            print(res)
            lamparas = Lampara.objects.all()
            return render(request, "lamparaslista.html", {
                "lamparas": lamparas
            })