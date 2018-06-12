from rest_framework import generics, mixins, permissions

from .serializers import AddressSerializer
from .models import Address
from .permissions import IsAddressOwnerOrAdmin

from accounts.permissions import IsAdmin


class AddressList(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  generics.GenericAPIView):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsAdmin]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AddressCreate(mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AddressDetail(mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    generics.GenericAPIView):

    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsAddressOwnerOrAdmin]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)