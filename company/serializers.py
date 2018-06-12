from rest_framework import serializers

from .models import Company

from address.serializers import AddressSerializer
from address.models import Address


class CompanySerializer(serializers.ModelSerializer):

    #address = AddressSerializer(required=False)

    class Meta:
        model = Company
        fields = ('id', 'name', 'company_reg',) # 'sector', 'type') #, 'address')
        read_only_field = ('id',)

    def create(self, validated_data):

        #address_data = validated_data.pop('address')
        #address = Address.objects.create(**address_data)
        company = Company(**validated_data)
        #company.address = address
        company.save()

        return company
