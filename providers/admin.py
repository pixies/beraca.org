from django.contrib import admin
from .models import ProviderGeneralData, ProvideRawMaterial, ProviderHandlingType, ProviderHandlingDryMethod, \
                    ProviderHandlingDryLocation, ProviderHandlingStorageMaterial, ProviderHandlingStorageFloor, \
                    ProviderHandlingStorageType, ProviderCertifications, ProviderHandlingData


class ProviderGeneralDataAdmin(admin.ModelAdmin):
    fields = ['name', 'cnpj', 'activities', 'provider_start_date',
              'products', 'clients', 'certifications', 'production_system',
              'training', 'communities']
    search_fields = ['name', 'cnpj']
    icon = '<i class="material-icons">transfer_within_a_station</i>'


class ProviderCertificationAdmin(admin.ModelAdmin):
    search_fields = ['name']
    icon = '<i class="material-icons">insert_drive_file</i>'


class ProviderHandlingStorageTypeAdmin(admin.ModelAdmin):
    search_fields = ['storage_type']
    icon = '<i class="material-icons">vpn_key</i>'


class ProviderHandlingStorageFloorAdmin(admin.ModelAdmin):
    search_fields = ['floor_type']
    icon = '<i class="material-icons">vignette</i>'


class ProviderHandlingStorageMaterialAdmin(admin.ModelAdmin):
    search_fields = ['material_type']
    icon = '<i class="material-icons">filter_frames</i>'


class ProviderHandlingDryLocationAdmin(admin.ModelAdmin):
    search_fields = ['dry_location']
    icon = '<i class="material-icons">pin_drop</i>'


class ProviderHandlingDryMethodAdmin(admin.ModelAdmin):
    search_fields = ['dry_method']
    icon = '<i class="material-icons">wb_sunny</i>'


class ProviderHandlingTypeAdmin(admin.ModelAdmin):
    search_fields = ['handling_type']
    icon = '<i class="material-icons">settings_input_composite</i>'


class ProvideRawMaterialAdmin(admin.ModelAdmin):
    search_fields = ['raw_material_type']
    icon = '<i class="material-icons">bubble_chart</i>'


class ProviderHandlingDataAdmin(admin.ModelAdmin):
    search_fields = ['provider__name']
    icon = '<i class="material-icons">nfc</i>'


admin.site.register(ProviderGeneralData, ProviderGeneralDataAdmin)
admin.site.register(ProviderCertifications, ProviderCertificationAdmin)
admin.site.register(ProviderHandlingStorageType, ProviderHandlingStorageTypeAdmin)
admin.site.register(ProviderHandlingStorageFloor, ProviderHandlingStorageFloorAdmin)
admin.site.register(ProviderHandlingStorageMaterial, ProviderHandlingStorageMaterialAdmin)
admin.site.register(ProviderHandlingDryLocation, ProviderHandlingDryLocationAdmin)
admin.site.register(ProviderHandlingDryMethod, ProviderHandlingDryMethodAdmin)
admin.site.register(ProviderHandlingType, ProviderHandlingTypeAdmin)
admin.site.register(ProvideRawMaterial, ProvideRawMaterialAdmin)
admin.site.register(ProviderHandlingData, ProviderHandlingDataAdmin)

