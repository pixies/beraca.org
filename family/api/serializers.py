from django.utils.translation import ugettext_lazy as _

from rest_framework.serializers import (
    ModelSerializer,
)

from family.models import Family

class GeneralFamilySerializer(ModelSerializer):
    class Meta:
        model = Family
        fields = (
        'family_name',
        'interviewee_name',
        'leader_name',
        'leader_sex',
        'leader_phone',
        'email',
        'occupation',
        'images_license',
        'future_vision',
        'health_problems',
        'incoming_sources',
        'created_at',
        'updated_at'
        )

class GeneralFamilyDetailSerializer(ModelSerializer):

    class Meta:
        model = Family
        fields = (
            'family_name',
            'interviewee_name',
            'leader_name',
            'leader_sex',
            'leader_phone',
            'email',
            'occupation',
            'images_license',
            'future_vision',
            'health_problems',
            'incoming_sources',
            'created_at',
            'updated_at'
        )
        read_only_fields = ('id',)
"""
    def update(self, instance, validated_data):
        address = instance.address
        address_data = validated_data.get('address')
        address.street = address_data.get('street', address.street)
        address.complement = address_data.get('complement', address.complement)
        address.post_code = address_data.get('post_code', address.post_code)
        address.city = address_data.get('city', address.city)
        address.state = address_data.get('state', address.state)
        address.country = address_data.get('country', address.country)
        address.save()

        instance.image = validated_data.get('image', instance.image)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.address = address
        instance.save()
"""