from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, generics, response, mixins
from django.shortcuts import get_object_or_404

from .models import UserNet
from .serializers import GetUserNetSerializer, GetUserNetPublicSerializer

from django.http import HttpResponse

def index(request):
    return HttpResponse("Это страница заглушка.")

class UserNetPublicView(ModelViewSet):
    """ Вывод публичного профиля пользователя
    """
    queryset = UserNet.objects.all()
    serializer_class = GetUserNetPublicSerializer
    permission_classes = [permissions.AllowAny]

class UserNetPrivateView(generics.RetrieveUpdateAPIView):
    """ Вывод профиля пользователя
    """
    serializer_class = GetUserNetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserNet.objects.filter(id=self.request.user.id)

    def get_object(self):
        obj = get_object_or_404(self.get_queryset())
        self.check_object_permissions(self.request, obj)
        return obj
