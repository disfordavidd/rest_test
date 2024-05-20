from django.urls import path
from David import views


urlpatterns = [
    path('sillas/', views.silla_list.as_view()),
    path('sillas/<int:pk>/', views.silla_detail.as_view()),
]
