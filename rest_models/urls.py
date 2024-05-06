from django.urls import path
from rest_models import views
from rest_framework.urlpatterns import format_suffix_patterns #Permite traer urls con extension html o json

urlpatterns = [
    path('items/', views.item_list.as_view()),
    path('items/<int:pk>/', views.item_detail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)