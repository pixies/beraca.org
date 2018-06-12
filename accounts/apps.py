from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AccountsConfig(AppConfig):
    name = 'accounts'
    verbose_name = _("Contas de usuário")
    icon = '<i class="material-icons">account_box</i>'
