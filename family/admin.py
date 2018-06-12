from django.contrib import admin
from .models import (
    Family,
    FamilySourcesIncome,
    FamilySourcesIncomeType,

    FamilyPictures,
    FamilyHealthProblem,
    FamilyDemography,
    FamilyInformationAboutChildrenTeenage,
    FamilyPropertyInformation,
    FamilyHousing,
    FamilyCommercialization,


    #Configure Family Housing info
    VegetationType,
    BuldingType,
    FloorType,
    CoverageType,

    #Configure Saneamento e Infra
    WaterSupplyType,
    WasteType,
    SolidWasteType,
    EletricyType,
    AccessPropertyType,

    # Configure Family Comercial Relations
    CommercializationRelationshipType,
    PeriodYearMostWorkCommercializationType,
    UsesInputsType,

    # Configure Family Manegements
    SelectsSeedsCollectionType,
    DriesCollectedSeedsType,
    PeelSollectedSeedsType,
    DifficultiesSeedSelectionType,
    StorageMethodType,
    StoringFloorType,
    StorageMaterialType,
    PreservationQualityHygieneStorageType,
    PlaceDryingType,
    MethodDryingType,
    FloorCanvasType,
    GreenhouseFloorType,
    GreenhouseCoverageType,
    PreservationQualityHygieneDryingType,
    ManagementType
)

"""
    Family
"""
class FamilyAdmin(admin.ModelAdmin):
    model = Family
    search_fields = ('family_name', 'leader_name', 'email')
    icon = '<i class="material-icons">domain</i>'

admin.site.register(Family, FamilyAdmin)

"""
    FamilySourcesIncome
        Fields:
            source of income type
"""
class FamilySourcesAdmin(admin.ModelAdmin):
    model = FamilySourcesIncome
    icon = '<i class="material-icons">attach_money</i>'

class FamilySourcesAdminType(admin.ModelAdmin):
    model = FamilySourcesIncomeType
    icon = '<i class="material-icons">attach_money</i>'

admin.site.register(FamilySourcesIncome, FamilySourcesAdmin)
admin.site.register(FamilySourcesIncomeType, FamilySourcesAdminType)


"""
    FamilyPictures
"""
class FamilyPicturesAdmin(admin.ModelAdmin):
    model = FamilyPictures
    icon = '<i class="material-icons">insert_photo</i>'

admin.site.register(FamilyPictures, FamilyPicturesAdmin)

"""
    FamilyHealthProblem
"""
class FamilyHealthProblemAdmin(admin.ModelAdmin):
    model = FamilyHealthProblem
    icon = '<i class="material-icons">healing</i>'

admin.site.register(FamilyHealthProblem, FamilyHealthProblemAdmin)

"""
    FamilyDemography
"""
class FamilyDemographyAdmin(admin.ModelAdmin):
    model = FamilyDemography
    icon = '<i class="material-icons">trending_up</i>'
    search_fields = ('family__family_name', )

admin.site.register(FamilyDemography, FamilyDemographyAdmin)

"""
    FamilyInformationAboutChildrenTeenage
"""
class FamilyInformationAboutChildrenTeenageAdmin(admin.ModelAdmin):
    model = FamilyInformationAboutChildrenTeenage
    icon = '<i class="material-icons">child_friendly</i>'
    list_display = ('family', 'number_children')
    search_fields = ('family__family_name', )

admin.site.register(FamilyInformationAboutChildrenTeenage, FamilyInformationAboutChildrenTeenageAdmin)


"""
    FamilyPropertyInformation
"""
class FamilyPropertyInformationAdmin(admin.ModelAdmin):
    model = FamilyPropertyInformation
    icon = '<i class="material-icons">info</i>'
    search_fields = ('family__family_name', )

admin.site.register(FamilyPropertyInformation, FamilyPropertyInformationAdmin)


"""
    FamilyHousing
        Fields:
            VegetationType
            BuildingType
            FloorType
            CoverageType
"""


class VegetationTypeAdmin(admin.ModelAdmin):
    model = VegetationType
    icon = '<i class="material-icons">local_florist</i>'


admin.site.register(VegetationType, VegetationTypeAdmin)


class BuildingTypeAdmin(admin.ModelAdmin):
    model = BuldingType
    icon = '<i class="material-icons">store_mall_directory</i>'


admin.site.register(BuldingType, BuildingTypeAdmin)

class FloorTypeAdmin(admin.ModelAdmin):
    model = FloorType
    icon = '<i class="material-icons">line_style</i>'

admin.site.register(FloorType, FloorTypeAdmin)


class CoverageTypeAdmin(admin.ModelAdmin):
    model = CoverageType
    icon = '<i class="material-icons">home</i>'

admin.site.register(CoverageType, CoverageTypeAdmin)

class FamilyHousingAdmin(admin.ModelAdmin):
    model = FamilyHousing
    icon = '<i class="material-icons">home</i>'

admin.site.register(FamilyHousing, FamilyHousingAdmin)


"""
    SanitationInfrastructure
        Fields:
            WaterSupplyType
            WasteType
            SolidWasteType
            EletricyType
            AccessPropertyType
"""
class WaterSupplyTypeAdmin(admin.ModelAdmin):
    model = WaterSupplyType
    icon = '<i class="material-icons">settings</i>'

class WasteTypeAdmin(admin.ModelAdmin):
    model = WasteType
    icon = '<i class="material-icons">hot_tub</i>'

class SolidWasteTypeAdmin(admin.ModelAdmin):
    model = SolidWasteType
    icon = '<i class="material-icons">view_stream</i>'

class EletricyTypeAdmin(admin.ModelAdmin):
    model = EletricyType
    icon = '<i class="material-icons">settings_input_svideo</i>'

class AccessPropertyTypeAdmin(admin.ModelAdmin):
    model = AccessPropertyType
    icon = '<i class="material-icons">blur_off</i>'

admin.site.register(WaterSupplyType, WaterSupplyTypeAdmin)
admin.site.register(WasteType, WasteTypeAdmin)
admin.site.register(SolidWasteType, SolidWasteTypeAdmin)
admin.site.register(EletricyType, EletricyTypeAdmin)
admin.site.register(AccessPropertyType, AccessPropertyTypeAdmin)

"""
    Family Commercialization Configurations
        Fields:
            Commercialization relationship
            What period of the year do you most work in marketing?
            Uses inputs
"""
class FamilyCommercializationAdmin(admin.ModelAdmin):
    model = FamilyCommercialization
    icon = '<i class="material-icons">business</i>'

class CommercializationRelationshipTypeAdmin(admin.ModelAdmin):
    model = CommercializationRelationshipType
    icon = '<i class="material-icons">playlist_add</i>'

class PeriodYearMostWorkCommercializationTypeAdmin(admin.ModelAdmin):
    model = PeriodYearMostWorkCommercializationType
    icon = '<i class="material-icons">perm_contact_calendar</i>'

class UsesInputsTypeAdmin(admin.ModelAdmin):
    model = UsesInputsType
    icon = '<i class="material-icons">web</i>'

admin.site.register(FamilyCommercialization, FamilyCommercializationAdmin)
admin.site.register(CommercializationRelationshipType, CommercializationRelationshipTypeAdmin)
admin.site.register(PeriodYearMostWorkCommercializationType, PeriodYearMostWorkCommercializationTypeAdmin)
admin.site.register(UsesInputsType, UsesInputsTypeAdmin)

"""
    Family Manegements
        Fields:
            SelectsSeedsCollectionType
            DriesCollectedSeedsType
            PeelSollectedSeedsType
            DifficultiesSeedSelectionType
            StorageMethodType
"""

class SelectsSeedsCollectionTypeAdmin(admin.ModelAdmin):
    model = SelectsSeedsCollectionType
    icon = '<i class="material-icons">select_all</i>'

admin.site.register(SelectsSeedsCollectionType, SelectsSeedsCollectionTypeAdmin)

class DriesCollectedSeedsTypeAdmin(admin.ModelAdmin):
    model = DriesCollectedSeedsType
    icon = '<i class="material-icons">spa</i>'

admin.site.register(DriesCollectedSeedsType, DriesCollectedSeedsTypeAdmin)

class PeelSollectedSeedsTypeAdmin(admin.ModelAdmin):
    model = PeelSollectedSeedsType
    icon = '<i class="material-icons">pan_tool</i>'

admin.site.register(PeelSollectedSeedsType, PeelSollectedSeedsTypeAdmin)

class DifficultiesSeedSelectionTypeAdmin(admin.ModelAdmin):
    model = DifficultiesSeedSelectionType
    icon = '<i class="material-icons">select_all</i>'

admin.site.register(DifficultiesSeedSelectionType, DifficultiesSeedSelectionTypeAdmin)

class StorageMethodTypeAdmin(admin.ModelAdmin):
    model = StorageMethodType
    icon = '<i class="material-icons">present_to_all</i>'

admin.site.register(StorageMethodType, StorageMethodTypeAdmin)

class StoringFloorTypeAdmin(admin.ModelAdmin):
    model = StoringFloorType
    icon = '<i class="material-icons">space_bar</i>'

admin.site.register(StoringFloorType, StoringFloorTypeAdmin)


class StorageMaterialTypeAdmin(admin.ModelAdmin):
    model = StorageMaterialType
    icon = '<i class="material-icons">widgets</i>'

admin.site.register(StorageMaterialType, StorageMaterialTypeAdmin)

class PreservationQualityHygieneStorageTypeAdmin(admin.ModelAdmin):
    model = PreservationQualityHygieneStorageType
    icon = '<i class="material-icons">repeat</i>'

admin.site.register(PreservationQualityHygieneStorageType, PreservationQualityHygieneStorageTypeAdmin)

class PlaceDryingTypeAdmin(admin.ModelAdmin):
    model = PlaceDryingType
    icon = '<i class="material-icons">wb_sunny</i>'

admin.site.register(PlaceDryingType, PlaceDryingTypeAdmin)

class MethodDryingTypeAdmin(admin.ModelAdmin):
    model = MethodDryingType
    icon = '<i class="material-icons">wb_iridescent</i>'

admin.site.register(MethodDryingType, MethodDryingTypeAdmin)

class FloorCanvasTypeAdmin(admin.ModelAdmin):
    model = FloorCanvasType
    icon = '<i class="material-icons">short_text</i>'

admin.site.register(FloorCanvasType, FloorCanvasTypeAdmin)

class GreenhouseFloorTypeAdmin(admin.ModelAdmin):
    model = GreenhouseFloorType
    icon = '<i class="material-icons">tonality</i>'

admin.site.register(GreenhouseFloorType, GreenhouseFloorTypeAdmin)

class GreenhouseCoverageTypeAdmin(admin.ModelAdmin):
    model = GreenhouseCoverageType
    icon = '<i class="material-icons">terrain</i>'

admin.site.register(GreenhouseCoverageType, GreenhouseCoverageTypeAdmin)

class PreservationQualityHygieneDryingTypeAdmin(admin.ModelAdmin):
    model = PreservationQualityHygieneDryingType
    icon = '<i class="material-icons">nature_people</i>'

admin.site.register(PreservationQualityHygieneDryingType, PreservationQualityHygieneDryingTypeAdmin)

class ManagementTypeAdmin(admin.ModelAdmin):
    model = ManagementType
    icon = '<i class="material-icons">toys</i>'

admin.site.register(ManagementType, ManagementTypeAdmin)
