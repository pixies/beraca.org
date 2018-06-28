from django.conf.urls import url, include


from rest_framework.urlpatterns import format_suffix_patterns

"""
from client.views import ProfileList, ProfileDetail, ProfileCreate,\
                   ClientList, ClientDetail, ClientCreate, get_products_per_client, get_projects_per_client, index
"""

from client.views import search, projeto_detalhe, apoio_project

from . import views

urlpatterns = [
    url(r'^search/', search, name='search'),
    url(r'^projeto/(?P<pk>[0-9]+)/$', projeto_detalhe, name='indexd'),
    #url(r'^projeto/suporte/$', project_support, name='indedxd'),
    url(r'^apoio_project/(?P<pk>[0-9]+)/(?P<pk2>[0-9]+)$', apoio_project, name='apoio_project'),
#    url('^', include('django.contrib.auth.urls')),
    #url(r'^.well-known/pki-validation/godaddy.html$', views.home, name='home'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
