from rest_framework import serializers

from .models import Address


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = ('id', 'street', 'complement', 'post_code', 'city', 'state', 'country',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        address_data = validated_data
        address = Address.objects.create(**address_data)

        return address

    def update(self, instance, validated_data):
        address_data = validated_data
        instance.street = address_data.get('street')
        instance.complement = address_data.get('complement')
        instance.post_code = address_data.get('post_code')
        instance.city = address_data.get('city')
        instance.state = address_data.get('state')
        instance.country = address_data.get('country')
        instance.save()

        return instance