from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class FamilyConfig(AppConfig):
    name = 'family'
    verbose_name = _('Famílias')
