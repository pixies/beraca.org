from django.contrib import admin
from .models import Project, ProjectCategory, ProjectPicture, ProjectcSupport


class PictureInline(admin.TabularInline):
    model = ProjectPicture


class ProjectcSupportAdmin(admin.ModelAdmin):
    model = ProjectcSupport
    list_display = ('project', 'client', 'status')
    search_fields = ['project', 'client']
    #icon = '<i class="material-icons">library_books</i>'


class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        PictureInline
    ]
    list_display = ['name', 'project_totals', 'community']
    search_fields = ['title', 'taxes']
    icon = '<i class="material-icons">library_books</i>'


class ProjectCategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    icon = '<i class="material-icons">loyalty</i>'


class ProjectPictureAdmin(admin.ModelAdmin):
    search_fields = ['name']
    icon = '<i class="material-icons">insert_photo</i>'


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectcSupport, ProjectcSupportAdmin)
admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(ProjectPicture, ProjectPictureAdmin)