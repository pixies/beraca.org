from django.db import models
from django.utils.translation import ugettext_lazy as _

from .constants import EPI_CHOICES, EPI_ORIGIN_CHOICES, HYGIENE_CHOICES, DRY_ROOF_TYPE_CHOICES

from client.models import Client
from product.models import Product
from community.models import Community


class ProviderCertifications(models.Model):
    name = models.CharField(_("Nome da certificação"), max_length=255, blank=False)
    valid_to = models.DateTimeField(_("Validade"), help_text=_("Válida até. Ex: 15/03/2019"), blank=True, null=True)
    registered_at = models.DateField(_("Data do registro"),
                                     help_text=_("Data referente ao registro da certificação"),
                                     blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Certificação")
        verbose_name_plural = _("Certificações")
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class ProviderGeneralData(models.Model):
    name = models.CharField(_("Nome"), max_length=255, blank=False)
    cnpj = models.CharField(_("CNPJ"), max_length=30, blank=True, null=True)
    activities = models.TextField(_("Atividades"), blank=True, null=True, help_text=_("Atividades da instituição"))
    provider_start_date = models.DateField(_("Início das atividades"), blank=True, null=True,
                                           help_text=_("Ano do início do fornecimento comercial da entidade"))
    products = models.ManyToManyField(Product, verbose_name=_("Produtos"), related_name="provider_products",
                                      help_text=_("Espécies de produtos fornecidos"),
                                      blank=True)
    clients = models.ManyToManyField(Client, verbose_name=_("Clientes"), related_name="client_providers",
                                     help_text=_("Clientes para o qual fornece"),
                                     blank=True)
    certifications = models.ManyToManyField(ProviderCertifications, verbose_name=_("Certificações"),
                                            help_text=_("Certificações que o fornecedor possui"),
                                            blank=True)
    production_system = models.TextField(_("Sistema de produção"), blank=True, null=True,
                                         help_text=_("Descritivo sobre o sistema de produção do fornecedor"))
    training = models.TextField(_("Capacitações"), blank=True, null=True,
                                help_text=_("Capacitações recebidas pela instituição"))
    communities = models.ManyToManyField(Community, verbose_name=_("Comunidades"),
                                         related_name="community_providers",
                                         help_text=_("Comunidades com as quais trabalha"),
                                         blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Fornecedor")
        verbose_name_plural = _("Fornecedores")

    def __str__(self):
        return self.name


class ProviderHandlingStorageType(models.Model):
    storage_type = models.CharField(_("Tipo de armazenamento"), max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Tipo de armazenamento")
        verbose_name_plural = _("Tipos de armazenamento")
        ordering = ['-created_at']

    def __str__(self):
        return self.storage_type


class ProviderHandlingStorageFloor(models.Model):
    floor_type = models.CharField(_("Piso utilizado no armazenamento"), max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Piso (armazenamento)")
        verbose_name_plural = _("Pisos (armazenamento)")
        ordering = ['-created_at']

    def __str__(self):
        return self.floor_type


class ProviderHandlingStorageMaterial(models.Model):
    material_type = models.CharField(_("Material utilizado no armazenamento"), max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Material (armazenamento)")
        verbose_name_plural = _("Materiais (armazenamento)")
        ordering = ['-created_at']

    def __str__(self):
        return self.material_type


class ProviderHandlingDryLocation(models.Model):
    floor_type = models.CharField(_("Piso utilizado na secagem"), choices=DRY_ROOF_TYPE_CHOICES,
                                  max_length=255, blank=False)
    roof_type = models.CharField(_("Teto utilizado na secagem (caso haja)"), max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Local (secagem)")
        verbose_name_plural = _("Locais (secagem)")
        ordering = ['-created_at']

    def __str__(self):
        if self.floor_type and self.roof_type:
            name = [self.floor_type, self.roof_type]
            return ", ".join(name)
        else:
            return self.floor_type


class ProviderHandlingDryMethod(models.Model):
    dry_method = models.CharField(_("Método utilizado na secagem"), max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Método de secagem")
        verbose_name_plural = _("Métodos de secagem")
        ordering = ['-created_at']

    def __str__(self):
        return self.dry_method


class ProviderHandlingType(models.Model):
    handling_type = models.CharField(_("Tipo de manejo"), max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Manejo (tipo)")
        verbose_name_plural = _("Manejos (tipos)")
        ordering = ['-created_at']

    def __str__(self):
        return self.handling_type


class ProvideRawMaterial(models.Model):
    raw_material_type = models.CharField(_("Tipo de matéria prima"), max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Tipo de matéria prima")
        verbose_name_plural = _("Tipos de matéria prima")
        ordering = ['-created_at']

    def __str__(self):
        return self.raw_material_type


class ProviderHandlingData(models.Model):
    provider = models.ForeignKey(ProviderGeneralData, verbose_name=_("Fornecedor"), blank=False,
                                 related_name='handling_data')
    uses_epi = models.CharField(_("EPI's"), max_length=255, choices=EPI_CHOICES,
                                help_text=_("Utiliza de EPI's na colheita/coleta?"),
                                blank=True, null=True)
    epi_origin = models.CharField(_("Origem da EPI"), max_length=255, choices=EPI_ORIGIN_CHOICES,
                                  help_text=_("Como adquiriu os EPI's utilizados na colheita/coleta (caso utilize)"),
                                  blank=True, null=True)
    selects_seeds = models.BooleanField(_("Seleciona as sementes?"),
                                        help_text=_("Marque caso o fornecedor selecione as sementes"))
    dries_seeds = models.BooleanField(_("Seca as sementes?"),
                                      help_text=_("Marque caso o fornecedor seque as sementes"))
    peels_seeds = models.BooleanField(_("Descasca as sementes?"),
                                      help_text=_("Marque caso o fornecedor descasque as sementes"))
    difficult_in_selection = models.BooleanField(_("Dificuldades na seleção?"),
                                                 help_text=_("Marque caso o fornecedor tenha dificuldades \
                                                 na seleção das sementes"))
    difficult_reason = models.TextField(_("Razão da dificuldade"),
                                        help_text=_("Motivo da dificuldade na seleção (caso haja)"),
                                        blank=True, null=True)
    storage_type = models.ForeignKey(ProviderHandlingStorageType, verbose_name=_("Tipo de armazenamento"),
                                     help_text=_("Informação sobre o método de armazenamento utilizado no produto"),
                                     blank=True, null=True)
    storage_floor = models.ForeignKey(ProviderHandlingStorageFloor, verbose_name=_("Tipo de piso utilizado no \
                                      armazenamento"),
                                      help_text=_("Informação sobre o piso que é utilizado no\
                                       armazenamento do produto"),
                                      blank=True, null=True)
    storage_material = models.ForeignKey(ProviderHandlingStorageMaterial,
                                         verbose_name=_("Tipo de material utilizado no armazenamento"),
                                         help_text=_("Informação referente ao material \
                                         utilizado no armazenamento do produto"),
                                         null=True, blank=True)
    used_material_reason = models.TextField(_("Razão de utilização do material"),
                                            help_text=_("Motivo da utilização de determinado material"),
                                            null=True, blank=True)
    storage_hygiene = models.CharField(_("Higiene/Preservação do armazenamento"), max_length=255,
                                       choices=HYGIENE_CHOICES, help_text=_("Informação referente higiene \
                                       e preservação de qualidade do produto"),
                                       null=True, blank=True)
    dry_location = models.ForeignKey(ProviderHandlingDryLocation, verbose_name=_("Local de secagem (caso haja)"),
                                     help_text=_("Informação referente ao local da secagem"),
                                     blank=True, null=True)
    dry_method = models.ForeignKey(ProviderHandlingDryMethod, verbose_name=_("Método de secagem (caso haja)"),
                                   help_text=_("Informação sobre \
                                   o método de secagem utilizado (caso seja utilizado algum)"),
                                   null=True, blank=True)
    dry_hygiene = models.CharField(_("Higiene/Preservação da secagem"), max_length=255, choices=HYGIENE_CHOICES,
                                   help_text=_("Inormação referente a higiene e preservação de qualidade do produto"),
                                   blank=True, null=True)
    handling_type = models.ForeignKey(ProviderHandlingType, verbose_name=_("Tipo de manejo"),
                                      help_text=_("informações sobre o manejo do produto"),
                                      blank=True, null=True)
    raw_material = models.ManyToManyField(ProvideRawMaterial, verbose_name=_("Tipo de matéria prima"),
                                          help_text=_("Informação sobre o tipo de matéria prima utilizada no produto"),
                                          blank=True)
    locomotion = models.TextField(_("Meio de locomoção"),
                                  help_text=_("Informação sobre o meio de locomoção até o consumidor"),
                                  null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Manejo (fornecedor)")
        verbose_name_plural = _("Manejos (fornecedores)")
        ordering = ['-created_at']

    def __str__(self):
        return self.provider.name
