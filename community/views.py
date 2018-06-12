from rest_framework import generics, mixins, permissions

from accounts.permissions import IsManagerOrAdmin, IsManagerClientOrAdmin, IsClientOrAdmin

from .models import Community
from .serializers import CommunitySerializer, CommunityListSerializer


class CommunityCreate(mixins.CreateModelMixin,
                      generics.GenericAPIView):
    http_method_names = ['post']
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsManagerOrAdmin]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CommunityList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    http_method_names = ['get']
    queryset = Community.objects.all()
    serializer_class = CommunityListSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CommunityDetail(mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      generics.GenericAPIView):
    http_method_names = ['get']
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsManagerClientOrAdmin]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CommunityUpdate(mixins.UpdateModelMixin,
                      mixins.RetrieveModelMixin,
                      generics.GenericAPIView):
    http_method_names = ['get', 'put']
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsManagerOrAdmin]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)