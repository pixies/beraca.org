from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _
from rest_framework.validators import UniqueValidator, ValidationError

from django.contrib.auth.models import User
from client.models import Profile, Client
from company.models import Company
from company.serializers import CompanySerializer

from rest_framework.serializers import (
    EmailField,
    CharField,
    ModelSerializer,
    PrimaryKeyRelatedField
)

User = get_user_model()

class UserCreateSerializer(ModelSerializer):

    company = CompanySerializer()
    full_name = CharField(label=_('Full Name'), max_length=255)

    class Meta:
        model = User
        fields = ('id', 'full_name', 'phone', 'email', 'password', 'company',)
        read_only_fields = ('id',)

    def create_client(self, user, company):
        Client.objects.create(user=user, company=company)

    def create(self, validated_data):

        company_data = validated_data.pop('company')
        company = Company.objects.create(**company_data)

        full_name = validated_data.pop('full_name')
        full_name = full_name.split()
        first_name = full_name[0]
        try:
            last_name = full_name[1]
        except IndexError:
            raise ValidationError('Por favor informe seu nome completo')
        phone = validated_data.pop('phone')
        user = User.objects.create_user(**validated_data)
        user.full_name = first_name + ' ' + last_name
        user.first_name = first_name
        user.last_name = last_name
        user.phone = phone
        user.company = company_data
        user.save()
        self.create_client(user, company)
        return user

class UserSerializer(ModelSerializer):

    profile = PrimaryKeyRelatedField(queryset=Profile.objects.all())
    client = PrimaryKeyRelatedField(queryset=Client.objects.all())

    class Meta:
        model = User
        fields = ('id', 'email', 'profile', 'client')
        read_only_fields = ('id',)

class UserListSerializer(ModelSerializer):
    """
        List resgistered Users
    """
    class Meta:
        model = User
        fields = ('id', 'email')


class UserUpdateSerializer(ModelSerializer):
    """
        Update registered User
    """
    class Meta:
        model = User
        fields = (
            'password'
        )