from django.db import models
from django.utils.translation import ugettext_lazy as _

from address.models import Address


class Company(models.Model):
    name = models.CharField(_("Nome"), max_length=255, blank=False)
    company_reg = models.CharField(_("CNPJ"), max_length=255, blank=False)
    sector = models.CharField(_("Setor"), max_length=255, blank=True)
    type = models.CharField(_("Tipo"), max_length=255, blank=True)
    #address = models.OneToOneField(Address, verbose_name=_("Endereço"),
    #                               max_length=255, blank=True,
    #                               related_name="company"
    #                               )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Empresa")
        verbose_name_plural = _("Empresas")
        ordering = ['-created_at']

    def __str__(self):
        return self.name

