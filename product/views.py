from django.db.models import Q
from rest_framework import generics, mixins, permissions, response

from accounts.permissions import IsClientOrAdmin, IsAdmin, IsManagerOrAdmin

from .serializers import ProductSerializer, ProductSearchSerializer
from .models import Product


class ProductList(mixins.ListModelMixin,
                  generics.GenericAPIView):
    http_method_names = ['get']
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
                          #IsClientOrAdmin]

    def get(self, request, *args, **kwargs):
        if 'names' in request.GET:
            queryset = self.get_queryset()
            queryset = queryset.values('id', 'scientific_name', 'common_name')
            serializer = ProductSearchSerializer(queryset, many=True)
            return response.Response(serializer.data)

        return self.list(request, *args, **kwargs)


class ProductCreate(mixins.CreateModelMixin,
                    generics.GenericAPIView):
    http_method_names = ['post']
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [ permissions.AllowAny,] #permissions.IsAuthenticated,
    #                      IsAdmin]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetail(mixins.RetrieveModelMixin,
                    generics.GenericAPIView):
    http_method_names = ['get']
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny,]
                          #IsClientOrAdmin]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ProductUpdate(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    http_method_names = ['get', 'put', 'delete']
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny,]
                          #IsManagerOrAdmin]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
