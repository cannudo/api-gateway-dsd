from django.urls import path
from etiqueta import views

# DELETAR

urlpatterns = [
    path('', views.EtiquetaViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy', 'put': 'update'})),
]