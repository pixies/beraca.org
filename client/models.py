from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _

User = get_user_model()

from address.models import Address
from company.models import Company
from product.models import Product

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=_("Usuário"),
                                on_delete=models.CASCADE,
                                related_name='profile')
    image = models.ImageField(_("Imagem do perfil"),
                              upload_to='accounts/profile/',
                              blank=True, null=True)
    birth_date = models.DateField(_("Data de nascimento"), blank=False)
    is_support = models.BooleanField(_("Técnico"))
    is_manager = models.BooleanField(_("Gestor"))
    is_admin = models.BooleanField(_("Administrador"))
    address = models.OneToOneField(Address, verbose_name=_("Endereço"),
                                   on_delete=models.CASCADE,
                                   related_name='profile')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Perfil")
        verbose_name_plural = _("Perfis")
        ordering = ['-created_at']

    def __str__(self):
        return self.user.get_full_name()

class Client(models.Model):
    user = models.OneToOneField(User, verbose_name=_("Cliente"),
                                on_delete=models.CASCADE,
                                related_name='client')
    company = models.ForeignKey(Company, verbose_name=_("Empresa"),
                                   on_delete=models.CASCADE,
                                   related_name="clients")

    products = models.ManyToManyField(Product, verbose_name=_("Produtos"), blank=True, null=True)
                                      #related_name="products", blank=True)

    #from project.models import Project
    #projects = models.ManyToManyField(Project, verbose_name=_("Projetos"), blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Cliente")
        verbose_name_plural = _("Clientes")
        ordering = ['-created_at']

    def __str__(self):
        return str(self.user)

    def get_products(self):
        return self.products.all()

    def get_project(self, product_id):
        from project.models import Project

        projects = Project.objects.all().filter(products__in=product_id)
        print(projects)
#        return "\n".join([p.common_name for p in self.projects.all()])

    #def get_products_in_project(self):
    #    p=self.projects.get(pk=2)
        #return "\n".join([self.projects.get(pk=2)])