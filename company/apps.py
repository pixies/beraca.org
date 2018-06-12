from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CompanyConfig(AppConfig):
    name = 'company'
    verbose_name = _("Empresas")
    icon = '<i class="material-icons">domain</i>'

