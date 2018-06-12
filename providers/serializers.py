from rest_framework import serializers
from .models import ProviderGeneralData


class ProviderGeneralDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProviderGeneralData
        fields = ('id', 'name', 'cnpj', 'activities', 'provider_start_date',
                  'products', 'clients', 'certifications', 'production_system',
                  'training', 'communities', 'created_at', 'updated_at', 'handling_data')
        read_only_fields = ['id', 'created_at']
