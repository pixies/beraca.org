from django.contrib import admin
from .models import Profile, Client


class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    icon = '<i class="material-icons">account_circle</i>'


class ClientAdmin(admin.ModelAdmin):
    model = Client
    verbose_name = 'Cliente'
#    projects = Client.Project.name

    list_display = ['user', 'company', 'get_products'] #, 'get_products']
    icon = '<i class="material-icons">account_box</i>'


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Client, ClientAdmin)
