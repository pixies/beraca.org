from django.contrib.auth import get_user_model

from .serializer import UserCreateSerializer, UserListSerializer, UserSerializer, UserUpdateSerializer
from django.utils.translation import ugettext_lazy as _
from libib.elasticemail import SendElastic

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    GenericAPIView,
)

from rest_framework.mixins import (
    CreateModelMixin
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
)


User = get_user_model() #Return User Model
class UserCreateAPIView(CreateModelMixin, GenericAPIView):

    http_method_names = ['post', ]
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        user_create = self.create(request, *args, **kwargs)
        # sent notification to user created successfully
        """
            E-mail dados
                subject: E-mail subject
                from_mail: Who sign the message
                to: recipient
                message:
        """
        subject = 'Seja bem vindo a Repartição de Benefícios!'
        to = str(user_create.data['email'])
        full_name = str(user_create.data['full_name'])

        message = """
                    Ola {0},

                    Seja bem vindo a Repartição de Benefícios do Instituto Beraca, este é apenas um e-mail para informar que sua conta foi criada com sucesso e que já pode utilizar nossa plataforma.

                    Obrigado,
                """.format(full_name)

        print(user_create.data['email'])

        print(SendElastic(subject, to, message))

        return user_create


class UserListAPIView(ListAPIView):
    """
        API for Lister Users
    """
    http_method_names = ['get', ]
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]

class UserDetailAPIView(RetrieveAPIView):
    """
        API for User detail
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]

class UserUpdateAPIVew(UpdateAPIView):
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)