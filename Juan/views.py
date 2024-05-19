from django.shortcuts import render
from django.conf import settings
from .models import Lampara
from .forms import LamparaForm

import requests

# Create your views here.
def lamparas(request):
    if request.method == "GET":
        lamparas = Lampara.objects.all()
        return render(request, "lamparaslista.html", {
            "lamparas": lamparas
        })
    
    elif request.method == "POST":
        if request.POST["_method"] == "DELETE":
            print("Eliminar elemento")
            res = requests.delete(settings.SITE_URL+request.POST["endpoint"])

            print(res)
            lamparas = Lampara.objects.all()
            return render(request, "lamparaslista.html", {
                "lamparas": lamparas
            })
        
def lamparaNueva(request):
    if request.method == "GET":
        return render(request, "nuevalampara.html", {
            "form": LamparaForm
        })
    
    elif request.method == "POST":
        res = requests.post(settings.SITE_URL+"/api/lampara/", data=request.POST)
        lamparas = Lampara.objects.all()
        return render(request, "lamparaslista.html", {
            "lamparas": lamparas
        })
    
def lamparaEditar(request):
    if request.method == "POST" and "_method" in request.POST:
        if request.POST["_method"] == "PUT":
            print("Actualizando elemento...")
            res = requests.put(settings.SITE_URL+request.POST["endpoint"], data=request.POST)
            print(res.status_code)
            print(res.content)
            lamparas = Lampara.objects.all()
            return render(request, "lamparaslista.html", {
                "lamparas": lamparas
            })
    elif request.method == "POST":
        res = requests.get(settings.SITE_URL+"/api/lampara/"+request.POST["lampara"])
        #print(res.json())
        return render(request, "editarlampara.html", {
            "form": LamparaForm(res.json()),
            "lampid": request.POST["lampara"]
        })