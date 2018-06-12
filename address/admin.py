from django.contrib import admin
from .models import Address


class AddressAdmin(admin.ModelAdmin):
    search_fields = ['street', 'cep', 'state']
    icon = '<i class="material-icons">pin_drop</i>'


admin.site.register(Address, AddressAdmin)
