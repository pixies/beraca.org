from django.db import models
from django.utils.translation import ugettext_lazy as _

from .constants import PROVENANCE_TYPE, COLLECTION_TYPE, BS_CHOICES, MONTHS_CHOICES


class ProductCollectionPoint(models.Model):
    location_type = models.CharField(_("Local da coleta/colheita"), max_length=255,
                                     blank=False, choices=COLLECTION_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Local de coleta/colheita")
        verbose_name_plural = _("Locais de coleta/colheita")
        ordering = ["-created_at"]

    def __str__(self):
        return self.location_type


class ProductHarvestPeriod(models.Model):
    harvest_period = models.CharField(_("Período"), max_length=255,
                                      blank=False, choices=MONTHS_CHOICES,
                                      unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Período da safra")
        verbose_name_plural = _("Períodos de safra")
        ordering = ["-created_at"]

    def __str__(self):
        return self.harvest_period


class Product(models.Model):
    scientific_name = models.CharField(_("Nome científico"), max_length=255,
                                       blank=True, null=True)
    common_name = models.CharField(_("Nome popular"), max_length=255, blank=False)
    provenance = models.CharField(_("Procedência"), max_length=255, blank=True, null=True,
                                  choices=PROVENANCE_TYPE)
    is_threatened = models.BooleanField(_("Espécie ameaçada?"), blank=True)
    fruit_anual_volume = models.PositiveIntegerField(_("Voume anual do fruto"),
                                                     default=0, help_text=_("Em KG"))
    seed_anual_volume = models.PositiveIntegerField(_("Voume anual da semente"),
                                                    default=0, help_text=_("Em KG"))
    pulp_anual_volume = models.PositiveIntegerField(_("Voume anual da polpa"),
                                                    default=0, help_text=_("Em KG"))
    harvest_period = models.ManyToManyField(ProductHarvestPeriod, verbose_name=_("Período da safra"),
                                            blank=True,
                                            help_text=_("Informações sobre o período da safra"))
    certification_origin = models.TextField(_("Orgão da certificação"), blank=True, null=True,
                                            help_text=_("Informações sobre o orgão que expediu\
                                                        a certificação do produto."))
    benefit_sharing_value = models.CharField(_("Regra de repartição de benefício"), max_length=255,
                                             blank=True, null=True, choices=BS_CHOICES)
    collection_point = models.ForeignKey(ProductCollectionPoint, verbose_name=_("Local de coleta/colheita"),
                                         related_name='products_collect', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Produto")
        verbose_name_plural = _("Produtos")
        ordering = ["-created_at"]

    def __str__(self):
        return self.common_name
