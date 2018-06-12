from django.db import models
from django.utils.translation import ugettext_lazy as _

from product.models import Product
from .constants import (
    SEX_CHOICES,
    LAND_SITUATION_CHOICES,
    HAS_CAR_CHOICES,
    GEOREFERENCING_CHOICES,
    AGE_GROUP_CHOICES,
    SCHOLL_BUS_CHOICES,
    NEGOTIATION_PRECESS_CHOICES,
    UNDERSTAND_PROCESS_BUY_RAW_MATERIAL_CHOICES,
    HAS_PURCHASE_RECEIPT_CHOICES,
    UNDERSTAND_PURCHASE_RECEIPT_NOTES_CHOICES,
    RECEIPT_FILING_CHOICES,
    SCANNING_FILES_CHOICES,
    DIFFICULTIES_TO_COMMERCIALIZE_CHOICES,
    SATISFACTION_WITH_STAGES_WORK_CHOICES,
    ORGANIC_CERTIFICATES_CHOICES,
    USE_EPI_CHOICES,
    HOW_GET_EPI_CHOICES,
    #SELECT_SEEDS_CHOICES
)

class FamilySourcesIncomeType(models.Model):

    source_income_type = models.CharField(verbose_name=_("Tipo de fonte de renda"), max_length=255)

    class Meta:
        verbose_name = _("Tipo Fonte de renda")
        verbose_name_plural = _("Tipos Fontes de renda")

    def __str__(self):
        return self.source_income_type


class FamilySourcesIncome(models.Model):
    """
        FamilySourcesIncome
        Fields:
            source of income type
            Monthly value
            Period of receipt of the source of income
            Annual value of the source of income
            Facts about banking
            Bank Credits
            Alternative credits
            Use of credits
    """

    source_income = models.ManyToManyField(FamilySourcesIncomeType,
                                                verbose_name=_("Tipo de fonte de renda"),
                                                help_text=_("Lista selecionável com os tipos de fontes de renda"),
                                                max_length=255,
                                                blank=False)

    monthly_value = models.CharField(verbose_name=_("Valor mensal da fonte de renda"),
                                     help_text=_("Valor recebido no período de um mês desta fonte de renda"),
                                     max_length=20,
                                     blank=True)

    period_receipt_source_income = models.CharField(verbose_name=_("Período de recebimento da fonte de renda"),
                                     help_text=_("Número de parcelas determinadas pelo período de recebimento desta fonte de renda (até 12 meses)"),
                                     max_length=2,
                                     blank=True)

    annual_value_source_income = models.CharField(verbose_name=_("Valor anual da fonte de renda"),
                                     help_text=_("Valor recebido no período de um ano desta fonte de renda (valor mensal multiplicado pelo período de recebimento)"),
                                     max_length=10,blank=True)

    facts_about_banking = models.CharField(verbose_name=_("Dados sobre situação bancária"),
                                     help_text=_("Quantos membros da família possuem contas bancárias"),
                                     max_length=2,blank=True)

    cank_credits = models.CharField(verbose_name=_("Créditos bancários"),
                                     help_text=_("Quantos membros da família possuem créditos em  banco"),
                                     max_length=2,blank=True)

    alternative_credits = models.CharField(verbose_name=_("Créditos alternativos"),
                                     help_text=_("Quantos membros da família possuem créditos alternativos"),
                                     max_length=2,blank=True)

    use_credits = models.TextField(verbose_name=_("Uso de Créditos"),
                                     help_text=_("Informação sobre a utilização dos créditos"),
                                     max_length=500,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Fonte de renda")
        verbose_name_plural = _("Fontes de renda")

    def __str__(self):
        return '{0} - {1} por Ano.'.format(self.source_income.values()[0]['source_income_type'], self.annual_value_source_income)

class FamilyHealthProblem(models.Model):
    health_problem = models.CharField(_("Tipo do problema de saúde"), max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Problema de saúde")
        verbose_name_plural = _("Problemas de saúde")

    def __str__(self):
        return self.health_problem

class Family(models.Model):
    """
    4.2 g.familia
    Fields:
        Family Name
        Name of respondent
        Name of representative
        Gender of the representative
        Age of representative
        Contact(Phone)
        Contact Us
        Occupation of the representative
        Source of income
        Photos
        Image Usage Authorization
        Cheers
        Future vision
    """
    family_name = models.CharField(verbose_name=_("Nome da família"),
                                   help_text=_("Nome da família"),
                                   max_length=255, blank=False)

    interviewee_name = models.CharField(verbose_name=_("Nome do entrevistado"),
                                        help_text=_("Nome do entrevistado da família"),
                                        max_length=255,
                                        blank=True, null=True)

    leader_name = models.CharField(verbose_name=_("Nome do líder da família"),
                                   help_text=_("Nome do representante da família"),
                                   max_length=255,
                                   blank=True,
                                   null=True)

    leader_sex = models.CharField(verbose_name=_("Sexo do líder da família"),
                                  help_text=_("Descrição de gênero"),
                                  max_length=255,
                                  choices=SEX_CHOICES,
                                  blank=True, null=True)

    age_leader =  models.IntegerField(verbose_name=_("Idade do líder da família"),
                                   help_text=_("Informação sobre a idade do representante da família"),
                                   )

    leader_phone = models.CharField(verbose_name=_("Telefone do líder da família"),
                                    help_text=_("Número de telefone do representante  da família (com DDD)"),
                                    max_length=50,
                                    blank=True, null=True)

    email = models.EmailField(verbose_name=_("Email para contato"),
                              help_text=_("Endereço de e-mail do representante  da família"),
                              blank=True, null=True)

    occupation = models.TextField(verbose_name=_("Ocupação"), blank=True, null=True,
                                  help_text=_("Descrição da ocupação atual do representante da família"))

    image_family = models.ImageField(verbose_name=_("Foto"),
                                      help_text=_("Fotos da família"),
                                      upload_to="family/pictures/%y/%m", blank=True, null=True)

    images_license = models.FileField(verbose_name=_("Licença de autorização de uso da imagem"),
                                      help_text=_("Documento com Autorização de Uso de Imagem"),
                                      upload_to="family/licenses/image/%m/%y", blank=True, null=True)

    future_vision = models.TextField(_("Visão de futuro"), blank=True, null=True,
                                     help_text=_("Descrição da visão de futuro da família"))

    health_problems = models.ManyToManyField(FamilyHealthProblem, verbose_name=_("Problemas de saúde"),
                                             help_text=_("Descrição das doenças crônicas e sobre condições de saúde da família "))

    sources_income = models.ManyToManyField(FamilySourcesIncome, verbose_name=_("Fontes de renda"),
                                         help_text=_("Descrição da principal fonte de renda do representante da família"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Família (dados gerais)")
        verbose_name_plural = _("Famílias (dados gerais)")
        ordering = ['-created_at']


    def __str__(self):
        return self.family_name

class FamilyPictures(models.Model):
    """
        4.2
        Familia: item.10
        linha: familia.fotos
    """
    from product.models import Product

    name = models.CharField(_("Nome da imagem"), max_length=255, blank=False)
    image = models.ImageField(_("Imagem"), upload_to="family/pictures/%y/%m", blank=False)
    product = models.ForeignKey(Product, verbose_name=_("Produto"), blank=False,
                                  related_name="product_images")

    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Imagem da família")
        verbose_name_plural = _("Imagens das famílias")
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.name

class FamilyDemography(models.Model):
    """
        4.2
        Demografia
    """

    family = models.OneToOneField(Family, verbose_name=_("Família relacionada"))
    man_number = models.PositiveIntegerField(_("Número de homens"), default=0,
                                             help_text=_("Quantidade de homens entre 18-65 anos da família"))
    woman_number = models.PositiveIntegerField(_("Número de mulheres"), default=0,
                                               help_text=_("Quantidade de mulheres entre 18-65 anos da família"))
    young_man_number = models.PositiveIntegerField(_("Número de homens jovens"), default=0,
                                                   help_text=_("Quantidade de homens entre 12-24 anos da família"))
    young_woman_number = models.PositiveIntegerField(_("Número de mulheres jovens"), default=0,
                                                     help_text=_("Quantidade de mulheres entre 12-24 anos da família"))
    kids_number = models.PositiveIntegerField(_("Número de crianças"), default=0,
                                              help_text=_("Quantidade de crianças da família"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = _("Demografia Famílias")
        verbose_name_plural = _("Demografia das Famílias")
        ordering = ['-created_at']


    def __str__(self):
        return self.family

class FamilyInformationAboutChildrenTeenage(models.Model):
    """
         4.2
         INFORMACAO SOBRE CRIANCA E ADOLECENTE
         INFORMATION ABOUT CHILDREN OR TEENAGER

        Fields:
            Age group
            Number of children
            Do not study and do not help
            Do not study and help
            Study
            How do they go to school?
            Study and help
            Study and work
            works
            Stays at home
            Collection area
            Processing area
            Cooperative / Association
            Community
            Responsible adult house
            Relatives house
            Comments

    """
    family = models.OneToOneField(Family, verbose_name=_("Família relacionada"))
    age_group = models.CharField(verbose_name=_("Faixa etária"),
                                 help_text=_("Lista de informações referente a faixa etária de cada criança/adolescente"),
                                 choices=AGE_GROUP_CHOICES,
                                 max_length=50
                                 )

    number_children = models.IntegerField(verbose_name=_("Quantidade de crianças"),
                                          help_text=_("Informação referente a quantidade de crianças/adolescentes na faixa etária selecionada.")
                                        ,)

    not_study_and_not_help = models.IntegerField(verbose_name=_("Não estuda e não ajudam"),
                                          help_text=_("Informação referente a quantidade de crianças/adolescentes que não estudam e não ajudam nas tarefas domésticas para faixa etária selecionada.")
                                        )
    not_study_and_help = models.IntegerField(verbose_name=_("Não estuda e ajudam"),
                                          help_text=_("Informação referente a quantidade de crianças/adolescentes que não estudam e ajudam nas tarefas domésticas para faixa etária selecionada.")
                                        )
    study = models.IntegerField(verbose_name=_("Estuda"),
                                          help_text=_("Informação referente a quantidade de crianças/adolescentes que estudam e não ajudam nas tarefas domésticas para faixa etária selecionada.")
                                        )
    how_do_they_go_to_school = models.CharField(verbose_name=_("Como vão a escola"),
                                                help_text=_("Lista de informações referente a meio de transporte utilizado para as crianças irem à escola"),
                                                choices=SCHOLL_BUS_CHOICES,
                                                max_length=80,
                                                null=True,
                                        )
    study_and_help = models.IntegerField(verbose_name=_("Estuda e ajuda"),
                                          help_text=_("Informação referente a quantidade de crianças/adolescentes que estudam e ajudam nas tarefas domésticas para faixa etária selecionada.")
                                        )
    study_and_work = models.IntegerField(verbose_name=_("Estuda e trabalha"),
                                         help_text=_("Informação referente a quantidade de crianças/adolescentes que estudam e trabalham  para faixa etária selecionada.")
                                         )
    work = models.IntegerField(verbose_name=_("Trabalha"),
                                         help_text=_("Informação referente a quantidade de crianças/adolescentes que não estudam e trabalham  para faixa etária selecionada.")
                                         )
    stays_at_home = models.IntegerField(verbose_name=_("Permanece em casa"),
                                         help_text=_("Informação referente a quantidade de crianças/adolescentes que fica em casa após a escola.")
                                         )
    collection_area = models.IntegerField(verbose_name=_("Área de coleta"),
                                         help_text=_("Informação referente a quantidade de crianças/adolescentes que fica vão para área de coleta após a escola.")
                                         )
    processing_area = models.IntegerField(verbose_name=_("Área de beneficiamento"),
                                         help_text=_("Informação referente a quantidade de crianças/adolescentes que fica vão para área de beneficiamento após a escola")
                                         )
    cooperative_association = models.IntegerField(verbose_name=_("Cooperativa/Associação"),
                                         help_text=_("Informação referente a quantidade de crianças/adolescentes que fica vão para cooperativa/associação após a escola")
                                         )
    community = models.IntegerField(verbose_name=_("Comunidade"),
                                         help_text=_("Informação referente a quantidade de crianças/adolescentes que vão comunidade após a escola")
                                         )
    responsible_adult_house = models.IntegerField(verbose_name=_("Casa de adulto responsável"),
                                         help_text=_("Informação referente a quantidade de crianças/adolescentes que fica vão para casa de um adulto responsável(e que não seja parente)  após a escola")
                                         )
    relatives_house = models.IntegerField(verbose_name=_("Casa de parentes"),
                                         help_text=_("Informação referente a quantidade de crianças/adolescentes que fica vão para casa de parentes  após a escola")
                                         )
    comments = models.TextField(verbose_name=_("Observações"),
                                help_text=_("Informação referente a alguma observação, caso seja necessário."),
                                )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Criança e adolescente")
        verbose_name_plural = _("Crianças e adolescentes")
        ordering = ['-created_at']

    def __str__(self):
        return self.family.family_name

class FamilyPropertyInformation(models.Model):
    """
     Informacao sobre Propriedade
    """
    family = models.OneToOneField(Family, verbose_name=_("Família relacionada"))

    land_situation = models.CharField(verbose_name=_("Situação Fundiária"),
                                      help_text=_("Lista de informações selecionáveis referentes à situação fundiária da família."),
                                      choices=LAND_SITUATION_CHOICES,
                                      max_length=50)
    total_size = models.CharField(verbose_name=_("Tamanho Total"),
                                  help_text=_("Tamanho da propriedade em hectares"),
                                  max_length=12)
    extractive_area = models.CharField(verbose_name=_("Área de Extrativismo"),
                                       help_text=_("Tamanho total da área de extrativismo utilizada em hectares"),
                                       max_length=9)
    forest_area = models.CharField(verbose_name=_("Área florestada"),
                                   help_text=_("Tamanho da área florestada antes e depois do extrativismo na propriedade, em hectares"),
                                   max_length=12)
    area_in_recovery = models.CharField(verbose_name=_("Área de Recuperação"),
                                        help_text=_("Tamanho da área em recuperação antes e depois do extrativismo na propriedade, em hectares"),
                                        max_length=12)
    deforest_area = models.CharField(verbose_name=_("Área Desmatada"),
                                     help_text=_("Tamanho da área desmatada antes e depois do extrativismo na propriedade, em hectares"),
                                     max_length=12)
    predominant_phytophysiognomy = models.TextField(verbose_name=_("Fitofisionomia predominante"),
                                                    help_text=_("Fitofisionomia (característica da vegetação) predominante na área com vegetação nativa conservada"),
                                                    max_length=1500)

    has_car = models.CharField(verbose_name=_("Possui CAR"),
                               help_text=_("A propriedade possui cadastro ambiental rural?"),
                               max_length=3,
                               choices=HAS_CAR_CHOICES)
    car_number = models.CharField(verbose_name=_("Número do CAR"),
                                  help_text=_("Número do Cadastro Ambiental Rural"),
                                  max_length=12)

    georeferencing = models.CharField(verbose_name=_("Georreferenciamento"),
                                      help_text=_("Tipo de georreferenciamento"),
                                      choices=GEOREFERENCING_CHOICES,
                                      max_length=100)

    previous_soil_use = models.TextField(verbose_name=_("Uso anterior do solo"),
                                         help_text=_("Uso do solo anterior ao fornecimento de matéria prima"),
                                         max_length=1500)
    soil_analysis_and_corrections = models.TextField(verbose_name=_("Análise do solo e correções"),
                                                     help_text=("Descritivo sobre frequência de análise do solo e correções aplicadas"),
                                                     max_length=1500)
    geotag_perimeter_latitude = models.CharField(verbose_name=_("GEOTAG Latitude"),
                                                 help_text=_("Dados de Latitude do perímetro da propriedade"),
                                                 max_length=20)

    geotag_perimeter_longitude = models.CharField(verbose_name=_("GEOTAG Longitude"),
                                                 help_text=_("Dados de Longitude do perímetro da propriedade"),
                                                 max_length=20)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Informação da Propriedade")
        verbose_name_plural = _("Informações da Propriedade")
        ordering = ['-created_at']

    def __str__(self):
        return "A situação da propriedade de {0} é {1}".format(self.family.family_name, self.load_situation)


"""
    Configuration area for Family Housing

        Type Vegetation
        type building
        type of floor
        Type of coverage

"""

class VegetationType(models.Model):
    """
        4.2
        Habitacao .item.1
        item: Perfil da Habitacao
        FamilyHousing.property_profile
    """

    vegetation = models.CharField(verbose_name=_("Tipo de vegetação"), max_length=200)

    class Meta:
        verbose_name = _("Tipo de Vegetação")
        verbose_name_plural = _("Tipos de Vegetação")

    def __str__(self):
        return self.vegetation

class BuldingType(models.Model):
    type_building = models.CharField(verbose_name=_('Tipo de Construção'),
                                     max_length=100,
                                     help_text=_("Informe o tipo construção da habitação.")
                                     )

    class Meta:
        verbose_name = _("Tipo de Construção")
        verbose_name_plural = _("Tipos de Construções")

    def __str__(self):
        return self.type_building

class FloorType(models.Model):
    type_floor = models.CharField(verbose_name=_('Tipo de piso'),
                                  max_length=100,
                                  help_text=_("Informe o tipo de piso da habitação.")
                                  )

    class Meta:
        verbose_name = _("Tipo de Piso")
        verbose_name_plural = _("Tipos de Piso")

    def __str__(self):
        return self.type_floor

class CoverageType(models.Model):
    type_coverage = models.CharField(verbose_name=_('Tipo de cobertura'),
                                     max_length=100,
                                     help_text=_("Informe o tipo de cobertura da habitação.")
                                     )

    class Meta:
        verbose_name = _("Tipo de Cobertura")
        verbose_name_plural = _("Tipos de Cobertura")

    def __str__(self):
        return self.type_coverage

class FamilyHousing(models.Model):

    CHOICES_OCCUPANCY_CONDITION = (
        ('PROPRIA', 'Própria'),
        ('ALUGADA', 'Alugada'),
        ('IRREGULAR', 'Iregular'),
        ('CEDIDA', 'Cedida')
    )

    family = models.OneToOneField(Family, verbose_name=_("Família relacionada"))

    property_profile = models.ManyToManyField(VegetationType, verbose_name=_("Tipo de vegetação"),
                                        help_text=_("Lista da informações selecionáveis referentes ao perfil da vegetação da propriedade"),
                                        )
    occupancy_condition = models.CharField(verbose_name=_("Tipo de ocupação"),
                                           max_length=50,
                                           help_text=_("Lista de informações selecionáveis referentes à situação de ocupação da família."),
                                           choices=CHOICES_OCCUPANCY_CONDITION)

    type_building = models.ManyToManyField(BuldingType, verbose_name=_("Tipo de construção"),
                                     help_text=_("Lista de informações selecionáveis referentes ao tipo de \
                                     construção da habitação."))

    type_floor = models.ManyToManyField(FloorType,
                                        verbose_name=_("Tipo de Piso"),
                                        help_text=_("Lista de informações selecionáveis referentes ao tipo de piso da habitação."))

    Type_coverage = models.ManyToManyField(CoverageType,
                                           verbose_name=_("Tipo de Cobertura"),
                                           help_text=_("Lista de informações selecionáveis referentes ao tipo de cobertura da habitação.")
                                           )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Habitação da Família")
        verbose_name_plural = _("Habitações da Familia")
        ordering = ['-created_at']

    def __str__(self):
        return "{0} mora em residência {1}".format(self.family.family_name, self.occupancy_condition)

"""
    Configuration area for Sanitation Infrastructure
    
        Water Supply
        Waste
        Solid Waste
        Electricity
        Access to the property
        Description of Access to the property
    
"""
class WaterSupplyType(models.Model):
    """
        Types of information about Water Supply
    """
    supply_type = models.CharField(verbose_name=_('Tipo de abastecimento água'),
                                   help_text=_('Situação de abastecimento de água da família'),
                                   max_length=100)

    class Meta:
        verbose_name = _("Tipo de Abastecimento de Água")
        verbose_name_plural = _("Tipos Abastecimento Água")

    def __str__(self):
        return self.supply_type

class WasteType(models.Model):
    """
        Types of information about Waste
    """
    waste_type = models.CharField(verbose_name=_('Tipo de dejetos'),
                                   help_text=_('Situação de  saneamento básico da família'),
                                   max_length=100)

    class Meta:
        verbose_name = _("Tipo de saneamento")
        verbose_name_plural = _("Tipos de saneamento")

    def __str__(self):
        return self.waste_type

class SolidWasteType(models.Model):
    """
        Types of information about Solid Waste
    """
    solid_waste_type = models.CharField(verbose_name=_('Tipo de Resíduos Sólidos'),
                                   help_text=_('Tipo de coleta de resíduos sólidos da família.'),
                                   max_length=100
                                )

    class Meta:
        verbose_name = _("Tipo de Resíduos Sólidos")
        verbose_name_plural = _("Tipos de Resíduos Sólidos")

    def __str__(self):
        return self.solid_waste_type

class EletricyType(models.Model):
    """
        Types of information about Eletricy
    """
    eletricy_type = models.CharField(verbose_name=_('Tipo de fonte de energia'),
                                   help_text=_('Tipo de fonte de energia elétrica da família'),
                                   max_length=100
                                )

    class Meta:
        verbose_name = _("Tipo de fonte de energia")
        verbose_name_plural = _("Tipos de fontes de energia")

    def __str__(self):
        return self.eletricy_type

class AccessPropertyType(models.Model):
    """
        Types of information about Access to the property
    """
    access_property_type = models.CharField(verbose_name=_('Tipo de acesso a propriedade'),
                                   help_text=_('Tipo de meio de transporte para acesso à residência da família.'),
                                   max_length=100
                                )

    class Meta:
        verbose_name = _("Tipo de acesso a propriedade")
        verbose_name_plural = _("Tipos de acessos a propriedade")

    def __str__(self):
        return self.access_property_type

class FamilySanitationInfrastructure(models.Model):

    family = models.OneToOneField(Family, verbose_name=_("Família relacionada"))

    water_supply = models.ManyToManyField(WaterSupplyType,
                                          verbose_name="Abastecimento de Água",
                                          help_text=_("Lista de informações selecionáveis referentes à situação de abastecimento de água da família.")
                                          )
    waste = models.ManyToManyField(WasteType,
                                verbose_name="Abastecimento de Água",
                                help_text=_("Lista de informações selecionáveis referentes à situação de saneamento básico da família."),
                                )
    solid_waste = models.ManyToManyField(SolidWasteType,
                                verbose_name="Resíduos Sólidos",
                                help_text=_("Lista de informações selecionáveis referentes ao tipo de coleta de resíduos sólidos da família."),
                                )

    eletricity = models.ManyToManyField(EletricyType,
                                verbose_name="Energia elétrica",
                                help_text=_("Lista de informações selecionáveis referentes ao tipo de fonte de energia elétrica da família."),
                                )

    access_property = models.ManyToManyField(AccessPropertyType,
                                verbose_name="Acesso à propriedade",
                                help_text=_("Lista de informações selecionáveis referentes ao tipo de meio de transporte para acesso à residência da família."),
                                )

    description_access_property = models.TextField(verbose_name=_("Descrição Acesso à propriedade"),
                                                   help_text=_("Descrição com informações de como chegar na propriedade"),
                                                   max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Saneamento e Infraestrutura")
        verbose_name_plural = _("Saneamento e Infraestrutura")
        ordering = ['-created_at']

    def __str__(self):
        return self.family

"""
    Family Commercialization Configurations
        Fields:
            Commercialization relationship
            What period of the year do you most work in marketing?
            Uses inputs
"""
class CommercializationRelationshipType(models.Model):

    commercialization_relationship_type = models.CharField(
        verbose_name=_("Relação de comercialização"),
        help_text=_("Tipo do formato da relação de comercialização da família."),
        max_length=50
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Tipo Rel. de Comercialização")
        verbose_name_plural = _("Tipos Rel. de Comercialização")
        ordering = ['-created_at']

    def __str__(self):
        return self.commercialization_relationship_type

class PeriodYearMostWorkCommercializationType(models.Model):

    period_year_most_work_commercialization_type = models.CharField(
        verbose_name=_("Meses do ano"),
        help_text=_("Lista dos meses que mais se trabalha na comercialização de produtos"),
        max_length=50
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Més do ano comercialização")
        verbose_name_plural = _("Meses do ano comercialização")
        ordering = ['-created_at']

    def __str__(self):
        return self.period_year_most_work_commercialization_type

class UsesInputsType(models.Model):

    uses_inputs_type = models.CharField(
        verbose_name=_("Lista de tipos insumos"),
        help_text=_("Tipos de informações selecionável referente a utilização de insumos"),
        max_length=60
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Tipo de insumo utilizado")
        verbose_name_plural = _("Tipos de insumos utilizados")
        ordering = ['-created_at']

    def __str__(self):
        return self.uses_inputs_type

class FamilyCommercialization(models.Model):
    """
        Fields:
            Commercialization relationship
            Degree of satisfaction of the commercialization
            Negotiation process?
            Degree of satisfaction in negotiation
            Do you understand the process of buying raw material?
            What are the doubts about the buying process?
            Has purchase receipt
            Do you understand the purchase receipt notes?
            What are the doubts about the receipt?
            Receipt filing
            How long the receipts are filed
            Scanning files
            Difficulties to commercialize
            Satisfaction with the stages of work
            What period of the year do you most work in marketing?
            Uses inputs
            Organic Certificates

    """
    family = models.OneToOneField(Family, verbose_name=_("Família relacionada"))

    commercialization_relationship = models.ManyToManyField(CommercializationRelationshipType,
                                                            verbose_name=_("Relação de comercialização"),
                                                            help_text=_("Lista de informações selecionáveis referentes ao formato da relação de comercialização da família.")
                                                            )
    degree_satisfaction_commercialization = models.TextField(verbose_name=_("Grau de satisfação da comercialização"),
                                                             help_text=_("Informação sobre o motivo da satisfação ou não com a comercialização"),
                                                             max_length=500)

    negotiation_process = models.CharField(verbose_name=_("Processo de Negociação"),
                                           help_text=_("Lista de informações selecionável referentes a satisfação com o processo de negociação"),
                                           max_length=3,
                                           choices=NEGOTIATION_PRECESS_CHOICES)

    degree_satisfaction_negotiation = models.TextField(verbose_name=_("Grau de satisfação na negociação"),
                                                             help_text=_("Informação sobre o motivo da satisfação ou não com a negociação"),
                                                             max_length=500)

    understand_process_buying_raw_material = models.CharField(verbose_name=_("Compreende o processo de compra de matéria prima?"),
                                           help_text=_("Lista de informações selecionável referentes a compreensão ou não do processo de compra de matéria prima"),
                                           max_length=3,
                                           choices=UNDERSTAND_PROCESS_BUY_RAW_MATERIAL_CHOICES)

    doubts_about_buying_process = models.TextField(verbose_name=_("Quais as dúvidas sobre o processo de compra?"),
                                                       help_text=_("Informação sobre as dúvidas referentes ao processo de compra de matéria prima"),
                                                       max_length=500)

    has_purchase_receipt = models.CharField(verbose_name=_("Possui recibo de compra"),
                                           help_text=_("Existe recibo de compra da matéria prima?"),
                                           max_length=15,
                                           choices=HAS_PURCHASE_RECEIPT_CHOICES)

    understand_purchase_receipt_notes = models.CharField(verbose_name=_("Compreende as anotações do recibo de compra?"),
                                           help_text=_("Lista de informações selecionável referentes à compreensão ou não das anotações do recibo de compra"),
                                           max_length=3,
                                           choices=UNDERSTAND_PURCHASE_RECEIPT_NOTES_CHOICES)

    what_doubts_about_receipt = models.TextField(verbose_name=_("Quais as dúvidas sobre o recibo?"),
                                                             help_text=_("Informação sobre as dúvidas referentes às anotações nos recibos de compra de matéria prima"),
                                                             max_length=500)

    receipt_filing = models.CharField(verbose_name=_("Arquivamento de recibos"),
                                           help_text=_("Os recibos de compra são arquivados?"),
                                           max_length=15,
                                           choices=RECEIPT_FILING_CHOICES)

    how_long_receipts_filed = models.IntegerField(verbose_name=_("Por quanto tempo os recibos são arquivados"),
                                                             help_text=_("Informação do tempo os recibos são guardados em meses")
                                                  )

    scanning_files = models.CharField(verbose_name=_("Digitalização dos arquivos"),
                                           help_text=_("Lista de informações selecionável referentes a digitalização de recibos arquivados"),
                                           max_length=3,
                                           choices=SCANNING_FILES_CHOICES)

    difficulties_to_commercialize = models.CharField(verbose_name=_("Dificuldades para comercializar"),
                                           help_text=_("Lista de informações selecionável referentes a comercialização do produto"),
                                           max_length=100,
                                           choices=DIFFICULTIES_TO_COMMERCIALIZE_CHOICES) # select field with other content field

    satisfaction_with_stages_work = models.CharField(verbose_name=_("Satisfação com as etapas do trabalho"),
                                           help_text=_("Lista de informações selecionável referentes a satisfação com as etapas de trabalho"),
                                           max_length=100,
                                           choices=SATISFACTION_WITH_STAGES_WORK_CHOICES)

    period_year_most_work_commercialization = models.ManyToManyField(PeriodYearMostWorkCommercializationType,
                                                                     verbose_name=_("Qual o período do ano mais trabalha na comercialização?"),
                                                                     help_text=_("Lista de informações selecionável referente aos meses que mais se trabalha na comercialização de produtos"),
                                                                     )
    uses_inputs = models.ManyToManyField(UsesInputsType,
                                         verbose_name=_("Utiliza insumos"),
                                         help_text=_("Lista de informações selecionável referente a utilização de insumos"),
                                         )
    organic_certificates = models.CharField(verbose_name=_("Certificados orgânicos"),
                                      help_text=_("Lista de informações selecionável referentes à certificação orgânica"),
                                      max_length=3,
                                      choices=ORGANIC_CERTIFICATES_CHOICES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Comercialização")
        verbose_name_plural = _("Comercializações")
        ordering = ['-created_at']

    def __str__(self):
        return self.family

class FamilyAgriculture(models.Model):
    """
        Fields:
            Subsistence products
            Commercialization products
    """

    family = models.OneToOneField(Family, verbose_name=_("Família relacionada"))

    subsistence_products = models.ManyToManyField(Product, related_name='agriculture_subsistence_common_name',
                                                  verbose_name=_("Produtos de subsistência"),
                                                  help_text=_("Lista de produtos de subsistência"))

    commercialization_products = models.ManyToManyField(Product, related_name='agriculture_commercialization_common_name',
                                                        verbose_name=_("Produtos de comercialização"),
                                                        help_text=_("Lista de produtos de comercialização"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Agricultura")
        verbose_name_plural = _("Agriculturas")
        ordering = ['-created_at']

    def __str__(self):
        return self.family

class FamilyExtractivist(models.Model):
    '''
        Fields:
            Subsistence products
            Marketing products
    '''
    family = models.OneToOneField(Family, verbose_name=_("Família relacionada"))

    subsistence_products = models.ManyToManyField(Product, related_name='extractivisti_subsistence_common_name',
                                                  verbose_name=_("Produtos de subsistência"),
                                                  help_text=_("Lista de produtos de subsistência"))

    commercialization_products = models.ManyToManyField(Product, related_name='extractivist_commercialization_common_name',
                                                        verbose_name=_("Produtos de comercialização"),
                                                        help_text=_("Lista de produtos de comercialização"))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Extrativismo")
        verbose_name_plural = _("Extrativismos")
        ordering = ['-created_at']

    def __str__(self):
        return self.family

"""
    Famili Management
        selects_seeds_collection
        dries_collected_seeds
"""
class SelectsSeedsCollectionType(models.Model):
    selects_seeds_collection_type = models.CharField(verbose_name=_("Seleciona sementes na coleta?"),
                                                help_text=_("Tipo de valores selecionáveis referente a seleção das sementes em local de coleta"),
                                                max_length=40,)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Seleção de semente")
        verbose_name_plural = _("Seleções de sementes")
        ordering = ['-created_at']

    def __str__(self):
        return self.selects_seeds_collection_type


class DriesCollectedSeedsType(models.Model):
    dries_collected_seeds_type = models.CharField(verbose_name=_("Seca as sementes coletadas?"),
                                                help_text=_("Lista de valores selecionáveis referente a secagem das sementes em local de coleta"),
                                                max_length=50,)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Seca a semente")
        verbose_name_plural = _("Seca as sementes")
        ordering = ['-created_at']

class PeelSollectedSeedsType(models.Model):
    peel_collected_seeds_type = models.CharField(verbose_name=_("Descasca as sementes coletadas?"),
                                                help_text=_("Lista de valores selecionáveis referente a descascagem das sementes em local de coleta"),
                                                max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Descasca a semente")
        verbose_name_plural = _("Descasca as sementes?")
        ordering = ['-created_at']

class DifficultiesSeedSelectionType(models.Model):

    difficulties_seed_selection_type = models.CharField(verbose_name=_("Dificuldades na seleção de sementes"),
                                                help_text=_("Lista de valores selecionáveis referente a dificuldade de seleção das sementes"),
                                                max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Dificuldade na seleção de semente")
        verbose_name_plural = _("Difícil seleção de sementes")
        ordering = ['-created_at']


class StorageMethodType(models.Model):
    storage_method_type = models.CharField(verbose_name=_("Método de Armazenamento"),
                                                help_text=_("Lista de valores selecionáveis com informações sobre o método de armazenamento utilizado no produto"),
                                                max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Método de Armazenamento")
        verbose_name_plural = _("Métodos de Armazenamento")
        ordering = ['-created_at']

class StoringFloorType(models.Model):
    storing_floor_type = models.CharField(verbose_name=_("Piso que Armazena"),
                                                help_text=_("Lista de valores selecionáveis com informações sobre o piso que armazena"),
                                                max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Piso que Armazena")
        verbose_name_plural = _("Pisos que Armazenam")
        ordering = ['-created_at']

class StorageMaterialType(models.Model):
    storing_floor_type = models.CharField(verbose_name=_("Material do Armazenameto"),
                                        help_text=_("Lista de valores selecionáveis com informações sobre o material do armazenamento"),
                                        max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Material do Armazenamento")
        verbose_name_plural = _("Materiais do Armazenamento")
        ordering = ['-created_at']

class PreservationQualityHygieneStorageType(models.Model):
    preservation_quality_hygiene_storage_type = models.CharField(verbose_name=_("Tipo de Preservação da qualidade e higiene no Armazenamento"),
                                        help_text=_("Lista de valores selecionáveis com informações sobre o material do armazenamento"),
                                        max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Tipo de preservação e higiene")
        verbose_name_plural = _("Tipos de preservação e higiene")
        ordering = ['-created_at']

class PlaceDryingType(models.Model):

    place_drying_type = models.CharField(verbose_name=_("Tipo de local de secagem"),
                                        help_text=_("Lista de valores selecionáveis sobre tipo de local de secagem"),
                                        max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Tipo de local de secagem")
        verbose_name_plural = _("Tipos de locais de secagem")
        ordering = ['-created_at']


class MethodDryingType(models.Model):

    method_drying_type = models.CharField(verbose_name=_("Método de secagem"),
                                        help_text=_("Lista de valores selecionáveis sobre tipo de método de secagem"),
                                        max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Tipo de método de secagem")
        verbose_name_plural = _("Tipos de metodos de secagem")
        ordering = ['-created_at']

class FloorCanvasType(models.Model):

    floor_canvas_type = models.CharField(verbose_name=_("Piso de Lona"),
                                        help_text=_("Lista de valores selecionáveis sobre tipo piso na lona"),
                                        max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Tipo de piso da lona")
        verbose_name_plural = _("Tipos de pisos da lona")
        ordering = ['-created_at']

class GreenhouseFloorType(models.Model):

    greenhouse_floor_type = models.CharField(verbose_name=_("Piso da estufa"),
                                        help_text=_("Lista de valores selecionáveis referente ao piso utilizado na Estufa (caso utilize Estufa)"),
                                        max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Tipo de piso da estufa")
        verbose_name_plural = _("Tipos de pisos da estufa")
        ordering = ['-created_at']

class GreenhouseCoverageType(models.Model):

    greenhouse_coverage_type = models.CharField(verbose_name=_("Tipo de cobertura da estufa"),
                                        help_text=_("Lista de valores selecionáveis referente a tipos cobertura utilizada na Estufa (caso utilize Estufa)"),
                                        max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Tipo de cobertura da estufa")
        verbose_name_plural = _("Tipos de cobertura da estufa")
        ordering = ['-created_at']


class PreservationQualityHygieneDryingType(models.Model):
    preservation_quality_hygiene_drying_type = models.CharField(verbose_name=_("Qualidade e Higiene do produto"),
                                        help_text=_("Valores selecionáveis referente a higiene e preservação de qualidade do produto"),
                                        max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Tipo da Qualidade e Higiene do produto")
        verbose_name_plural = _("Tipos da Qualidade e Higiene")
        ordering = ['-created_at']

class ManagementType(models.Model):
    management_type = models.CharField(verbose_name=_("Tipo de manejo"),
                                        help_text=_("Valores selecionáveis referente a tipos de manejo"),
                                        max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Tipo de Manejo")
        verbose_name_plural = _("Tipos de Manejo")
        ordering = ['-created_at']


class TypeRawMaterialType(models.Model):

    type_raw_material_type = models.CharField(verbose_name=_("Tipo de materia prima"),
                                        help_text=_("Lista de valores selecionáveis referente ao tipo de materia prima"),
                                        max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Tipo de Materia prima")
        verbose_name_plural = _("Tipos de Materia prima")
        ordering = ['-created_at']





class FamilyManagement(models.Model):
    """
        Fields:
            Uses EPI's
            How did you get EPI's?
            Selects seeds in the collection?
            Dries the collected seeds?
            Peel the collected seeds?
            Difficulties in seed selection
            Volume
            Storage method
            Storing floor
            Storage Material
            Reason for using the material
            Preservation of quality and hygiene - Storage
            Place of drying
            Method of drying
            Floor of the canvas
            Greenhouse Floor
            Greenhouse Coverage
            Preservation of quality and hygiene - Drying
            Management
            Type of raw material
            Means of transportation
    """

    family = models.OneToOneField(Family, verbose_name=_("Família relacionada"))

    uses_epis = models.CharField(verbose_name=_("Utiliza EPI's"),
                                 help_text=_("Lista de valores selecionáveis sobre a utilização de EPI's na colheita/coleta"),
                                 max_length=40,
                                 choices=USE_EPI_CHOICES)

    how_get_epis = models.CharField(verbose_name=_("Utiliza EPI's"),
                                 help_text=_("Lista de valores selecionáveis sobre a utilização de EPI's na colheita/coleta"),
                                 max_length=40,
                                 choices=HOW_GET_EPI_CHOICES)

    selects_seeds_collection = models.ForeignKey(SelectsSeedsCollectionType,
                                    verbose_name=_("Seleciona sementes na coleta?"),
                                    help_text=_("Lista de valores selecionáveis referente a seleção das sementes em local de coleta"),
                                    )

    dries_collected_seeds = models.ForeignKey(DriesCollectedSeedsType,
                                    verbose_name=_("Seca as sementes coletadas?"),
                                    help_text=_("Lista de valores selecionáveis referente a secagem das sementes em local de coleta"),
                                    )

    peel_collected_seeds = models.ForeignKey(PeelSollectedSeedsType,
                                    verbose_name=_("Descasca as sementes coletadas?"),
                                    help_text=_("Lista de valores selecionáveis referente a descascagem das sementes em local de coleta"),
                                    )

    difficulties_seed_selection = models.ManyToManyField(DifficultiesSeedSelectionType,
                                    verbose_name=_("Dificuldades na seleção"),
                                    help_text=_("Lista de valores selecionáveis referentes a dificuldade de seleção das sementes"),
                                    )

    volume = models.IntegerField(verbose_name=_("Volume"),
                                help_text=_("Informação sobre o volume do produto"),
                                 )

    storage_method = models.ManyToManyField(StorageMethodType,
                                    verbose_name=_("Métodos de Armzenamento"),
                                    help_text=_("Lista de valores selecionáveis com informações sobre o método de armazenamento utilizado no produto"),
                                    )

    storing_floor = models.ManyToManyField(StoringFloorType,
                                    verbose_name=_("Piso que armazena"),
                                    help_text=_("Lista de valores selecionáveis com informações sobre o piso que é utilizado no armazenamento do produto"),
                                    )

    storage_material = models.ManyToManyField(StorageMaterialType,
                                    verbose_name=_("Material do armazenamento"),
                                    help_text=_("Lista de valores selecionáveis com informações referente ao material utilizado no armazenamento do produto"),
                                    )

    reason_using_material = models.TextField(verbose_name=_("Motivo de utilização do material"),
                                 help_text=_("Informação sobre o motivo da utilização de determinado material"),
                                 max_length=500)

    preservation_quality_hygiene_storage = models.ForeignKey(PreservationQualityHygieneStorageType,
                                    verbose_name=_("Preservação da qualidade e higiene - Armazenamento"),
                                    help_text=_("Lista de valores selecionáveis referente higiene e preservação de qualidade do produto"),
                                    )

    place_drying = models.ForeignKey(PlaceDryingType,
                                    verbose_name=_("Local da secagem"),
                                    help_text=_("Lista de valores selecionáveis com informações referentes ao local da secagem"),
                                    )

    method_drying = models.ManyToManyField(MethodDryingType,
                                    verbose_name=_("Método de secagem"),
                                    help_text=_("Lista de valores selecionáveis sobre o método de secagem utilizado (caso seja utilizado algum)"),
                                    )

    floor_canvas = models.ManyToManyField(FloorCanvasType,
                                    verbose_name=_("Piso da Lona"),
                                    help_text=_("Lista de valores selecionáveis referente ao piso utilizado na Lona (caso utilize Lona)"),
                                    )

    greenhouse_floor = models.ManyToManyField(GreenhouseFloorType,
                                    verbose_name=_("Piso da Estufa"),
                                    help_text=_("Lista de valores selecionáveis referente ao piso utilizado na Estufa (caso utilize Estufa)"),
                                    )

    greenhouse_coverage = models.ForeignKey(GreenhouseCoverageType,
                                    verbose_name=_("Cobertura da Estufa"),
                                    help_text=_("Lista de valores selecionáveis referente a cobertura utilizada na Estufa (caso utilize Estufa)"),
                                    )

    preservation_quality_hygiene_drying = models.ForeignKey(PreservationQualityHygieneDryingType,
                                    verbose_name=_("Preservação da qualidade e higiene - Secagem"),
                                    help_text=_("Lista de valores selecionáveis referente higiene e preservação de qualidade do produto"),
                                    )

    management = models.ManyToManyField(ManagementType,
                                    verbose_name=_("Manejo"),
                                    help_text=_("Lista de valores selecionáveis com informações sobre o manejo do produto"),
                                    )

    type_raw_material = models.ManyToManyField(TypeRawMaterialType,
                                    verbose_name=_("Tipo de matéria prima"),
                                    help_text=_("Lista de valores selecionáveis com informações sobre o tipo de matéria prima utilizada no produto"),
                                    )

    means_transportation = models.TextField(verbose_name=_("Meio de locomoção"),
                                            help_text=_("Informação sobre o meio de locomoção até o comprador"),
                                            max_length=500)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Manejo")
        verbose_name_plural = _("Manejos")
        ordering = ['-created_at']

    def __str__(self):
        return self.family

class FamilyUrbanArea(models.Model):
    """
        Fields:
            Work in the urban area
            Description of the activity in the urban area
            Nature of activity
            Employer
    """
    pass

class FamilyHumanSocialCapital(models.Model):
    """
        Fields:
            Participation in meetings
            Type of activity involved
            Participation in training
            Training in new skills
            Are you interested in organizing yourself legally?
            Understand What is Organic Certification?
            Looking for information about activities and visits of technicians on Organic Certification in the community?
            Do you participate in Organic Certification?
            How do you participate in Organic Certification?
            Do you try to conform to Organic Certification?
            Why is it suitable for Organic Certification?
            Difficulty in understanding the organic certification process?
            Does the property work all year round?

    """

    pass

class FamilyComercialRelations(models.Model):
    """
        Fields:
            Nome do cliente
            Avaliação sobre rendimento
            Transparência na atividade
            Avaliação da extração
            Processos de pagamento
            Processos de entrega
            Impacto da parceria

    """
    pass
    
