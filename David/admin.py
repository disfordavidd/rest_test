"""
Admin de la aplicación David
"""

from django.contrib import admin
from David.models import Silla

"""
Registrar modelos de la aplicación David
"""

admin.site.register(Silla)
