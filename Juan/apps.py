"""
Configuración de la app Juan
"""

from django.apps import AppConfig


class JuanConfig(AppConfig):
    """ Atributos de configuración de la app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Juan'
