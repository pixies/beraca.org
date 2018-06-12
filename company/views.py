from rest_framework import mixins, generics, permissions

from accounts.permissions import IsClientOrAdmin, IsAdmin

from .models import Company
from .serializers import CompanySerializer
from .permissions import IsCompanyOwner


class CompanyList(mixins.ListModelMixin,
                  generics.GenericAPIView):
    http_method_names = ['get']
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsClientOrAdmin,
                          IsAdmin]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class CompanyCreate(mixins.CreateModelMixin,
                    generics.GenericAPIView):
    http_method_names = ['post']
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsClientOrAdmin]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CompanyUpdate(mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    http_method_names = ['get', 'put', 'delete']
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsClientOrAdmin,
                          IsCompanyOwner]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class CompanyDetail(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):

    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsClientOrAdmin,
                          IsCompanyOwner]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)