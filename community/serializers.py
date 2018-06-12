from rest_framework import serializers

from .models import Community, CommunityContacts, CommunityLeadership, CommunityLeadershipType,\
                    CommunityPicture, CommunitySchools, CommunityBiomes, CommunityBiomesPicture,\
                    CommunityCraftwork, CommunityCraftworkPicture

from address.models import Address
from address.serializers import AddressSerializer
from product.serializers import ProductSerializer, ProductSearchSerializer


class CommunityLeadershipTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommunityLeadershipType
        fields = ('id', 'description',)
        read_only_fields = ('id',)


class CommunityLeadershipSerializer(serializers.ModelSerializer):

    type = CommunityLeadershipTypeSerializer()

    class Meta:
        model = CommunityLeadership
        fields = ('id','name', 'phone', 'type',)
        read_only_fields = ('id',)


class CommunityContactsSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommunityContacts
        fields = ('id', 'name', 'phone', 'contact_type')
        read_only_fields = ('id',)


class CommunityPictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommunityPicture
        fields = ('id', 'name', 'image', 'community')
        read_only_fields = ('id',)


class CommunitySchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommunitySchools
        fields = ('id', 'name', 'levels', 'community')
        read_only_fields = ('id',)


class CommunityBiomesPictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommunityBiomesPicture
        fields = ('id', 'name', 'image', 'biome')
        read_only_fields = ('id',)


class CommunityBiomesSerializer(serializers.ModelSerializer):

    images = CommunityBiomesPictureSerializer(many=True)

    class Meta:
        model = CommunityBiomes
        fields = ('id', 'characteristics', 'type', 'threatened_species', 'phytophysionomy', 'ground_type',
                  'images')
        read_only_fields = ('id',)


class CommunityCraftworkPictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommunityCraftworkPicture
        fields = ('id', 'name', 'image', 'craftwork')


class CommunityCraftworkSerializer(serializers.ModelSerializer):
    images = CommunityCraftworkPictureSerializer(many=True)

    class Meta:
        model = CommunityCraftwork
        read_only_fields = ('id', 'name', 'price', 'community', 'images')


class CommunitySerializer(serializers.ModelSerializer):

    leadership = CommunityLeadershipSerializer()
    contacts = CommunityContactsSerializer(many=True)
    images = CommunityPictureSerializer(many=True)
    schools = CommunitySchoolSerializer(many=True)
    biomes = CommunityBiomesSerializer(many=True)
    craftworks = CommunityCraftworkSerializer(many=True)
    address = AddressSerializer()
    products = ProductSerializer(many=True)

    class Meta:
        model = Community
        fields = ('id', 'name', 'geo_lat', 'geo_long', 'distance_from_capital',
                  'idh_state', 'idh_city', 'energy_type', 'families_number',
                  'religion', 'traditional_culture', 'craftworks', 'traditional_events',
                  'sanctuaries', 'hospitals_number', 'ready_care_number', 'psf_number',
                  'address', 'leadership', 'products', 'contacts', 'images', 'schools',
                  'biomes')
        read_only_fields = ('id',)

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address = Address.objects.create(**address_data)

        community = Community(**validated_data)
        community.address = address
        community.save()

        leaderships_data = validated_data.pop('leadership')

        for leadership_data in leaderships_data:
            CommunityLeadership.objects.create(community=community, **leadership_data)

        contacts_data = validated_data.pop('contacts')

        for contact_data in contacts_data:
            CommunityContacts.objects.create(community=community, **contact_data)

        images_data = validated_data.pop('images')

        for image_data in images_data:
            CommunityPicture.objects.create(community=community, **image_data)

        schools_data = validated_data.pop('schools')

        for school_data in schools_data:
            CommunitySchools.objects.create(community=community, **school_data)

        biomes_data = validated_data.pop('biomes')

        for biome_data in biomes_data:
            CommunityBiomes.objects.create(community=community, **biome_data)

        craftworks_data = validated_data.pop('craftwork')

        for craftwork_data in craftworks_data:
            CommunityCraftwork.objects.create(community=community, **craftwork_data)

        return community


class CommunityListSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    images = CommunityPictureSerializer(many=True)

    class Meta:
        model = Community
        fields = ('name', 'address', 'images')


class CommunityProductListSerializer(serializers.ModelSerializer):
    products = ProductSearchSerializer(many=True)

    class Meta:
        model = Community
        fields = ('id' ,'name', 'products')
