from django.urls import include, path
from rest_framework import routers
from etiqueta import views

router = routers.DefaultRouter()
router.register(r'etiquetas', views.EtiquetaViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]