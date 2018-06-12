from rest_framework import generics, mixins, permissions

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from accounts.api.serializer import UserSerializer
from accounts.api.permissions import IsAdmin, IsClientOrAdmin, IsProfileOwner, IsClientOwner

User = get_user_model()

class UserList(mixins.ListModelMixin, generics.GenericAPIView):

    http_method_names = ['get', ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserCreate(mixins.CreateModelMixin, generics.GenericAPIView):
    http_method_names = ['post', ]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]

    def post(self, request, *args, **kwargs):
        user_create = self.create(request, *args, **kwargs)

        return user_create


class UserDetail(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    http_method_names = ['get', 'put', 'delete']
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



from django.http import HttpResponse
from django.shortcuts import render

def my_login(request):
    return HttpResponse('Login lll')

