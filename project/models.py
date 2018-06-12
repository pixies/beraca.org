from django.db import models
from django.utils.translation import ugettext_lazy as _

from community.models import Community
#from client.models import Client


class ProjectCategory(models.Model):
    name = models.CharField(_("Nome"), max_length=255, blank=True, unique=True)

    class Meta:
        verbose_name = _("Categoria de projeto")
        verbose_name_plural = _("Categorias de projeto")

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(_("Nome"), max_length=255, blank=False)
    target_area = models.TextField(_("Área de atuação"), blank=True, null=True)
    theme_description = models.TextField(_("Tema"), blank=True, null=True)
    goals = models.TextField(_("Objetivos"), blank=True, null=True)
    specific_goals = models.TextField(_("Objetivos específicos"), blank=True, null=True)
    activities = models.TextField(_("Atividades a serem desenvolvidas"), blank=True, null=True)
    results = models.TextField(_("Resultados esperados"), blank=True, null=True)
    schedule = models.FileField(_("Cronograma"),
                                upload_to="project/schedules/%y/%m", blank=True,
                                null=True, help_text=_("Arquivo PDF com o cronograma do projeto"))
    target_audience = models.TextField(_("Público alvo"), blank=True)
    budget = models.FileField(_("Orçamento"),
                              upload_to="project/budgets/%y/%m", blank=True,
                              null=True, help_text=_("Aquivo PDF com o orçamento do projeto"))
    project_totals = models.DecimalField(_("Valor total do projeto"),
                                         max_digits=20,
                                         decimal_places=2, blank=True, null=True)
    taxes = models.DecimalField(_("Valor do administrativo"),
                                max_digits=5,
                                decimal_places=2,
                                blank=True, null=True, help_text="Percentagem do valor do projeto que será destinado ao administrativo",)
    community_tour = models.BooleanField(_("Visita comunitária"),
                                         blank=True,
                                         help_text=_("Assinala caso seja projeto de visita\
                                                     comunitária"))
    future_vision = models.TextField(_("Visão de futuro"),
                                     blank=True, null=True,
                                     help_text=_("Breve resumo de qual seria a visão de futuro \
                                                 da comunidade com a execução do projeto."))

    category = models.ManyToManyField(ProjectCategory, verbose_name=_("Categorias"),
                                      related_name="project_categories", blank=True, null=True)

    community = models.ForeignKey(Community, verbose_name=_("Comunidade"), related_name="community_projects",
                                  blank=True, null=True)

#    from client.models import Client
#    client = models.ForeignKey(Client, verbose_name=_("Cliente apoiador"), related_name="supported_projects",
#                               blank=True, null=True)

    from product.models import Product
    products = models.ManyToManyField(Product, verbose_name=_("Produtos"),
                                      related_name="project_products", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Projeto")
        verbose_name_plural = _("Projetos")
        ordering = ["-created_at"]

    def __str__(self):
        return self.name

    def get_products(self):
        return "\n".join([p.common_name for p in self.products.all()])

    def get_category(self):
        return "\n".join([c.name for c in self.category.all()])

class ProjectPicture(models.Model):
    name = models.CharField(_("Nome da imagem"), max_length=255, blank=True)
    image = models.ImageField(_("Imagem"), upload_to="project/pictures/%y/%m", blank=True)
    project = models.ForeignKey(Project, verbose_name=_("Projeto    "), blank=True,
                                related_name="images")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _("Imagem do projeto")
        verbose_name_plural = _("Imagens do projeto")
        ordering = ['-uploaded_at']

    def __str__(self):
        return self.name

from client.models import Client

class ProjectcSupport(models.Model):

    project_support_id = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, verbose_name=_("Project"))
    client = models.ForeignKey(Client, verbose_name=_("Client"))
    status = models.BooleanField(default=False, verbose_name=_("I want to support"))

    class Meta:
        verbose_name = _('Projeto apoiado')
        verbose_name_plural = _('Projetos apoiados')

    def __str__(self):
        return str(self.project)
