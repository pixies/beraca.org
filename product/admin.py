from django.contrib import admin
from .models import Product, ProductCollectionPoint, ProductHarvestPeriod


class ProductHarvestPeriodAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">date_range</i>'


class ProductAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">spa</i>'
    search_fields = ['scientific_name', 'common_name']
    list_filter = ['provenance', 'benefit_sharing_value']
    list_display = ['common_name', 'scientific_name', 'collection_point', 'provenance',
                    'seed_anual_volume', 'pulp_anual_volume']


class ProductCollectionPointAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">pan_tool</i>'


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCollectionPoint, ProductCollectionPointAdmin)
admin.site.register(ProductHarvestPeriod, ProductHarvestPeriodAdmin)