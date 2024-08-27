from django.urls import include, path
from rest_framework import routers
from etiqueta import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'etiquetas', views.EtiquetaViewSet)

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("etiquetasfalha/", include('etiqueta.urls')),  # DELETAR
    path('', include(router.urls)),
]