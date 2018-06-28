from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from client.views import ProfileList, ProfileDetail, ProfileCreate,\
                   ClientList, ClientDetail, ClientCreate, get_products_per_client, get_projects_rates_per_client, index, get_categorie

urlpatterns = [
    # Profile - api/profile/
    url(r'^profile/list/$', ProfileList.as_view(), name='profile-list'),
    url(r'^profile/create/$', ProfileCreate.as_view(), name='profile-create'),
    url(r'^profile/detail/(?P<pk>[0-9]+)/$', ProfileDetail.as_view(), name='profile-detail'),

    # Client - api/client/
    url(r'^list/$', ClientList.as_view(), name='client-list'),
    url(r'^create/$', ClientCreate.as_view(), name='client-create'),
    url(r'^detail/(?P<pk>[0-9]+)/$', ClientDetail.as_view(), name='client-detail'),


    url(r'^index/$', index, name='index'),
    url(r'^get_projects/(?P<pk>[0-9]+)/$', get_projects_rates_per_client, name='project-suppot-d'),
    url(r'^get_products/$', get_products_per_client, name='project-support-d'),
    url(r'^get_categories/(?P<pk>.+)/$', get_categorie, name='project-suppor'),


]

urlpatterns = format_suffix_patterns(urlpatterns)