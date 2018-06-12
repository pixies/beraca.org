from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ProvidersConfig(AppConfig):
    name = 'providers'
    verbose_name = _("Fornecedores")
    icon = '<i class="material-icons">transfer_within_a_station</i>'
