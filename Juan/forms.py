from django.forms import ModelForm
from .models import Lampara

class LamparaForm(ModelForm):
    class Meta:
        model = Lampara
        fields = ['nombre','precio','cantidad','fecha']