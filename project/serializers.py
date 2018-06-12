from rest_framework import serializers

from .models import Project, ProjectCategory, ProjectPicture, ProjectcSupport

from community.serializers import CommunityProductListSerializer


class ProjectPictureSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectPicture
        fields = ('id', 'name', 'image', 'project')
        read_only_fields = ('id',)


class ProjectCategorySerializer(serializers.ModelSerializer):
    project_categories = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='project:project-detail')

    class Meta:
        model = ProjectCategory
        fields = ('id', 'name', 'project_categories')
        read_only_fields = ('id',)


class ProjectCategorySerializerNested(serializers.ModelSerializer):

    class Meta:
        model = ProjectCategory
        fields = ('id', 'name',)
        read_only_fields = ('id',)


class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectPictureSerializer(many=True, read_only=True)
    category = ProjectCategorySerializerNested(many=True)
    #community = CommunityProductListSerializer()

    from product.serializers import ProductSerializer
    products = ProductSerializer(many=True)

    class Meta:
        model = Project
        fields = ('id', 'name','target_area', 'theme_description', 'goals',
                  'specific_goals', 'activities', 'results', 'schedule',
                  'target_audience', 'project_totals', 'taxes',
                  'community_tour', 'future_vision', 'category', 'images', 'products', 'community'
                   )
        read_only_fields = ('id',)

    def create(self, validated_data):
        categories_data = validated_data.pop('category')
        project = Project.objects.create(**validated_data)

        for category_data in categories_data:
            category = ProjectCategory.objects.create(**category_data)
            project.category.add(category)

        return project


class ProjectSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectcSupport
        fields = ('project_support_id','project', 'client')


class ProjectListSerializer(serializers.ModelSerializer):

    images = ProjectPictureSerializer(many=True, read_only=True)
    category = ProjectCategorySerializerNested(many=True)
    community = CommunityProductListSerializer(many=True)

    from product.serializers import ProductSerializer
    products = ProductSerializer()

    class Meta:
        model = Project
        fields = ('id', 'name', 'target_area', 'theme_description', 'goals',
                  'specific_goals', 'activities', 'results', 'schedule',
                  'target_audience', 'project_totals', 'taxes',
                  'community_tour', 'future_vision', 'category', 'images', 'products',
                  'community')
        read_only_fields = ('id',)

    def create(self, validated_data):
        categories_data = validated_data.pop('category')
        project = Project.objects.create(**validated_data)

        for category_data in categories_data:
            category = ProjectCategory.objects.create(**category_data)
            project.category.add(category)

        return project