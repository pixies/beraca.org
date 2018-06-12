from django.db import models
from django.utils.translation import ugettext_lazy as _

from .constants import UF_CHOICES


class Address(models.Model):
    street = models.CharField(_("Rua"), max_length=255, blank=False)
    quartiere = models.CharField(_("Bairro"), max_length=255, blank=True, null=True)
    complement = models.CharField(_("Complemento"), max_length=255, blank=True, null=True)
    post_code = models.CharField(_("CEP"), max_length=15, blank=False)
    city = models.CharField(_("Cidade"), max_length=15, blank=False)
    state = models.CharField(_("Estado"), max_length=20, blank=False, choices=UF_CHOICES)
    country = models.CharField(_("País"), max_length=35, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Endereço")
        verbose_name_plural = _("Endereços")
        ordering = ['-created_at']

    def __str__(self):
        return '{0} - {1} - {2}/{3}'.format(self.street, self.quartiere, self.city, self.state)

