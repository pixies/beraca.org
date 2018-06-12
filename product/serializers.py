from rest_framework import serializers

from .models import Product, ProductCollectionPoint


class ProductCollectionPointSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCollectionPoint
        fields = ('id', 'location_type',)
        read_only_fields = ('id',)


class ProductSerializer(serializers.ModelSerializer):

    collection_point = ProductCollectionPointSerializer()

    class Meta:
        model = Product
        fields = ('id', 'scientific_name', 'common_name', 'provenance',
                  'is_threatened', 'fruit_anual_volume', 'seed_anual_volume',
                  'pulp_anual_volume', 'harvest_period', 'certification_origin',
                  'benefit_sharing_value', 'collection_point', 'communities')

        read_only_fields = ('id',)

    def create(self, validated_data):
        collection_data = validated_data.pop('collection_point')
        product = Product(**validated_data)
        collection_point = ProductCollectionPoint.objects.create(**collection_data)
        product.collection_point = collection_point
        product.save()

        return product


class ProductSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'scientific_name', 'common_name')
        read_only_fields = ('id', )

