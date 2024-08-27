from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from .models import Etiqueta
from .serializers import *
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

class EtiquetaViewSet(viewsets.ModelViewSet):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# DELETAR
@csrf_exempt
def etiqueta_list(request):
    if request.method == "GET":
        etiquetas = Etiqueta.objects.all()
        serializer = EtiquetaSerializer(etiquetas, many = True)
        json = JsonResponse(serializer.data, safe = False)
        return json
    return HttpResponse(200)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]