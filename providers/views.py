from rest_framework import generics, mixins, permissions

from accounts.permissions import IsManagerOrAdmin

from .models import ProviderGeneralData
from .serializers import ProviderGeneralDataSerializer


class ProviderListView(mixins.ListModelMixin,
                              generics.GenericAPIView):
    http_method_names = ['get', ]
    queryset = ProviderGeneralData.objects.all()
    serializer_class = ProviderGeneralDataSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsManagerOrAdmin]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ProviderCreateView(mixins.CreateModelMixin,
                         generics.GenericAPIView):
    http_method_names = ['post', ]
    queryset = ProviderGeneralData.objects.all()
    serializer_class = ProviderGeneralDataSerializer
    permissions = [permissions.IsAuthenticated,
                   IsManagerOrAdmin]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProviderUpdateView(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    http_method_names = ['get', 'put', 'delete']
    queryset = ProviderGeneralData.objects.all()
    serializer_class = ProviderGeneralDataSerializer
    permissions = [permissions.IsAuthenticated,
                   IsManagerOrAdmin]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)



