from django.shortcuts import render
from .models import Lampara

# Create your views here.
def lamparas(request):
    if request.method == "GET":
        lamparas = Lampara.objects.all()
        return render(request, "lamparaslista.html", {
            "lamparas": lamparas
        })