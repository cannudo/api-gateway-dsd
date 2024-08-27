from django.urls import path
from etiqueta import views

# DELETAR

urlpatterns = [
    path('', views.etiqueta_list),
]