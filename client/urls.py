from django.conf.urls import url, include


from rest_framework.urlpatterns import format_suffix_patterns

"""
from client.views import ProfileList, ProfileDetail, ProfileCreate,\
                   ClientList, ClientDetail, ClientCreate, get_products_per_client, get_projects_per_client, index
"""

from client.views import search, projeto_detalhe, project_support

urlpatterns = [
    url(r'^search/', search, name='search'),
    url(r'^projeto/(?P<pk>[0-9]+)/$', projeto_detalhe, name='indexd'),
    url(r'^projeto/suporte/$', project_support, name='indedxd'),
#    url('^', include('django.contrib.auth.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)