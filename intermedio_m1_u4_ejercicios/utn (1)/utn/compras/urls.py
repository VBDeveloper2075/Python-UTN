from django.urls import path
from compras import views

urlpatterns = [
    path('El_perro_corre', views.index, name='index'),
]
