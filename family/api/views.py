from family.api.serializers import GeneralFamilySerializer, GeneralFamilyDetailSerializer
from family.models import Family
from rest_framework import generics, mixins, permissions

class GeneralFamilyView(mixins.ListModelMixin,
                  generics.GenericAPIView):
    http_method_names = ['get', ]
    queryset = Family.objects.all()
    serializer_class = GeneralFamilySerializer
    permission_classes = [permissions.IsAuthenticated,]
                          #IsAdmin]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



class GeneralFamilyDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    http_method_names = ['get', 'put', 'delete']
    queryset = Family.objects.all()
    serializer_class = GeneralFamilyDetailSerializer
    permission_classes = [permissions.IsAuthenticated,]
                          #IsProfileOwner]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
