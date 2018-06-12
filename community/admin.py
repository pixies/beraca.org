from django.contrib import admin
from .models import CommunityLeadershipType, CommunityLeadership,\
    Community, CommunityContacts, CommunityPicture, CommunitySchools,\
    CommunityBiomes, CommunityBiomesPicture, CommunityCraftwork, CommunityCraftworkPicture


class CommunityContactsInline(admin.TabularInline):
    model = CommunityContacts


class CommunityPictureInline(admin.TabularInline):
    model = CommunityPicture


class CommunitySchoolsInline(admin.TabularInline):
    model = CommunitySchools


class CommunityBiomesInline(admin.StackedInline):
    model = CommunityBiomes


class CommunityCraftworkInline(admin.TabularInline):
    model = CommunityCraftwork


class CommunityCraftworkPictureInline(admin.TabularInline):
    model = CommunityCraftworkPicture


class CommunityAdmin(admin.ModelAdmin):
    inlines = [
        CommunityContactsInline,
        CommunityPictureInline,
        CommunitySchoolsInline,
        CommunityBiomesInline,
        CommunityCraftworkInline,
    ]
    search_fields = ["name",]
    icon = '<i class="material-icons">group_work</i>'


class CommunityBiomesPicturesInline(admin.TabularInline):
    model = CommunityBiomesPicture


class CommunityBiomesAdmin(admin.ModelAdmin):
    inlines = [
        CommunityBiomesPicturesInline
    ]
    search_fields = ["community__name",]
    icon = '<i class="material-icons">nature_people</i>'


class CommunityCraftworkAdmin(admin.ModelAdmin):
    inlines = [
        CommunityCraftworkPictureInline
    ]
    list_display = ('name', 'price', 'community')
    search_fields = ["community__name",]
    icon = '<i class="material-icons">build</i>'


class CommunityContactsAdmin(admin.ModelAdmin):
    search_fields = ['name']
    icon = '<i class="material-icons">contact_phone</i>'


class CommunityPictureAdmin(admin.ModelAdmin):
    search_fields = ['name']
    icon = '<i class="material-icons">insert_photo</i>'


class CommunityLeadershipAdmin(admin.ModelAdmin):
    search_fields = ['name']
    icon = '<i class="material-icons">accessibility</i>'


class CommunitySchoolsAdmin(admin.ModelAdmin):
    search_fields = ['name']
    icon = '<i class="material-icons">school</i>'


class CommunityBiomesPictureAdmin(admin.ModelAdmin):
    search_fields = ['name']
    icon = '<i class="material-icons">insert_photo</i>'


class CommunityCraftworkPictureAdmin(admin.ModelAdmin):
    search_fields = ['name']
    icon = '<i class="material-icons">domain</i>'


class CommunityLeadershipTypeAdmin(admin.ModelAdmin):
    icon = '<i class="material-icons">merge_type</i>'


admin.site.register(CommunityLeadershipType, CommunityLeadershipTypeAdmin)
admin.site.register(CommunityLeadership, CommunityLeadershipAdmin)
admin.site.register(Community, CommunityAdmin)
admin.site.register(CommunityContacts, CommunityContactsAdmin)
admin.site.register(CommunityPicture, CommunityPictureAdmin)
admin.site.register(CommunitySchools, CommunitySchoolsAdmin)
admin.site.register(CommunityBiomes, CommunityBiomesAdmin)
admin.site.register(CommunityBiomesPicture, CommunityPictureAdmin)
admin.site.register(CommunityCraftwork, CommunityCraftworkAdmin)
admin.site.register(CommunityCraftworkPicture, CommunityCraftworkPictureAdmin)