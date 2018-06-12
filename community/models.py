from django.db import models
from django.utils.translation import ugettext_lazy as _

from address.models import Address
from product.models import Product

from .constants import ENERGY_TYPE, SCHOOL_TYPE


class CommunityLeadershipType(models.Model):
    description = models.CharField(_("Tipo da liderança"), max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Tipo de liderança")
        verbose_name_plural = _("Tipos de liderança")
        ordering = ['-created_at']

    def __str__(self):
        return self.description


class CommunityLeadership(models.Model):
    name = models.CharField(_("Nome"), max_length=255, blank=False)
    phone = models.CharField(_("Telefone"), max_length=255, blank=False)
    type = models.ForeignKey(CommunityLeadershipType, verbose_name=_("Tipo de liderança"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Lider")
        verbose_name_plural = _("Lideres")
        ordering = ['-created_at']

    def __str__(self):
        return "{0} ({1})".format(self.name, self.type)


class Community(models.Model):
    name = models.CharField(_("Nome da comunidade"), max_length=255, blank=False)
    geo_lat = models.CharField(_("Latitude"), max_length=255, blank=True, null=True)
    geo_long = models.CharField(_("Longitude"), max_length=255, blank=True, null=True)
    distance_from_capital = models.CharField(_("Distância até a capital"), max_length=255,
                                             blank=True, null=True)
    idh_state = models.CharField(_("IDH do estado"), max_length=255, blank=True, null=True)
    idh_city = models.CharField(_("IDH da cidade"), max_length=255, blank=True, null=True)
    energy_type = models.CharField(_("Tipo de energia elétrica"), max_length=255,
                                   choices=ENERGY_TYPE, blank=True, null=True)
    families_number = models.PositiveIntegerField(_("Número de famílias"),
                                                  default=0, blank=True, null=True)
    religion = models.CharField(_("Religião predominante"),
                                max_length=255, blank=True, null=True)
    traditional_culture = models.TextField(_("Manifestações culturais"), blank=True, null=True)
    traditional_events = models.TextField(_("Festas típicas"), blank=True, null=True)
    sanctuaries = models.PositiveIntegerField(_("Número de templos"),
                                              blank=True, null=True,
                                              help_text=_("Número de templos religiosos na comunidade"),
                                              default=0)
    hospitals_number = models.PositiveIntegerField(_("Número de hospitais"), blank=True, null=True,
                                                   default=0)
    ready_care_number = models.PositiveIntegerField(_("Número de pronto atendimento"),
                                                    blank=True, null=True, default=0)
    psf_number = models.PositiveIntegerField(_("Número de psf's"), blank=True, null=True,
                                             default=0)
    address = models.ForeignKey(Address, verbose_name=_("Endereço"), related_name="community")
    leadership = models.ForeignKey(CommunityLeadership, verbose_name=_("Liderança"), blank=True, null=True)
    products = models.ManyToManyField(Product, verbose_name=_("Produtos"),
                                      related_name="communities", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Comunidade")
        verbose_name_plural = _("Comunidades")
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class CommunityCraftwork(models.Model):
    name = models.CharField(_("Nome do produto"), max_length=255, blank=False)
    price = models.DecimalField(_("Preço"), decimal_places=2, default=0, max_digits=4)
    community = models.ForeignKey(Community, verbose_name=_("Comunidade"), related_name="craftworks",
                                  on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Artesanato")
        verbose_name_plural = _("Artesenatos")
        ordering = ['-created_at']

    def __str__(self):
        return self.name

class CommunityCraftworkPicture(models.Model):
    name = models.CharField(_("Nome da imagem"), max_length=255, blank=False)
    image = models.ImageField(_("Imagem"), upload_to="community/craftwork/pictures/%y/%m", blank=False)
    craftwork = models.ForeignKey(CommunityCraftwork, verbose_name=_("Comunidade"), blank=False,
                                  related_name="images")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Imagem de artesanato")
        verbose_name_plural = _("Imagens de artesanato")
        ordering = ['-uploaded_at']

    def __str__(self):
        return '{0} comunidade {1}'.format(self.name, self.craftwork)


class CommunityContacts(models.Model):
    name = models.CharField(_("Nome do contato"), max_length=255, blank=False)
    phone = models.CharField(_("Telefone"), max_length=255, blank=False)
    contact_type = models.CharField(_("Tipo do contato"), max_length=255, blank=False)
    community = models.ForeignKey(Community, verbose_name=_("Comunidade"), related_name="contacts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Contato da comunidade")
        verbose_name_plural = _("Contatos da comunidade")
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class CommunityPicture(models.Model):
    name = models.CharField(_("Nome da imagem"), max_length=255, blank=False)
    image = models.ImageField(_("Imagem"), upload_to="community/pictures/%y/%m", blank=False)
    community = models.ForeignKey(Community, verbose_name=_("Comunidade"), blank=False,
                                  related_name="images")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Imagem da comunidade")
        verbose_name_plural = _("Imagens da comunidade")
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.name


class CommunitySchools(models.Model):
    name = models.CharField(_("Nome da escola"), max_length=255, blank=False)
    levels = models.CharField(_("Nível escolar máximo"), max_length=255, blank=False,
                              choices=SCHOOL_TYPE)
    community = models.ForeignKey(Community, verbose_name=_("Comunidade"), on_delete=models.CASCADE,
                                  related_name='schools')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Escola da comunidade")
        verbose_name_plural = _("Escolas da comunidade")
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class CommunityBiomes(models.Model):
    community = models.ForeignKey(Community, verbose_name=_("Comunidade"), related_name='biomes')
    characteristics = models.TextField(_("Características"), blank=False)
    type = models.TextField(_("Tipo do bioma"), blank=False)
    threatened_species = models.TextField(_("Lista de espécies ameaçadas"), blank=True, null=True)
    phytophysionomy = models.TextField(_("Fitofisionomia"), blank=True, null=True)
    ground_type = models.TextField(_("Tipo do solo"), blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Bioma da comunidade")
        verbose_name_plural = _("Biomas da comunidade")
        ordering = ['-created_at']

    def __str__(self):
        return self.characteristics


class CommunityBiomesPicture(models.Model):
    name = models.CharField(_("Nome da imagem"), max_length=255, blank=False)
    image = models.ImageField(_("Imagem"), upload_to="community/biomes/pictures/%y/%m", blank=False)
    biome = models.ForeignKey(CommunityBiomes, verbose_name=_("Bioma"), blank=False,
                              related_name="images")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Imagem do bioma")
        verbose_name_plural = _("Imagens do bioma")
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.name
