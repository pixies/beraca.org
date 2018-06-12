from django.contrib import admin
from .models import Company


class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['name']
    icon = '<i class="material-icons">domain</i>'


admin.site.register(Company, CompanyAdmin)
