from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from client.views import ProfileList, ProfileDetail, ProfileCreate,\
                   ClientList, ClientDetail, ClientCreate

urlpatterns = [
    # Profile - api/profile/
    url(r'^profile/list/$', ProfileList.as_view(), name='profile-list'),
    url(r'^profile/create/$', ProfileCreate.as_view(), name='profile-create'),
    url(r'^profile/detail/(?P<pk>[0-9]+)/$', ProfileDetail.as_view(), name='profile-detail'),

    # Client - api/client/
    url(r'^list/$', ClientList.as_view(), name='client-list'),
    url(r'^create/$', ClientCreate.as_view(), name='client-create'),
    url(r'^detail/(?P<pk>[0-9]+)/$', ClientDetail.as_view(), name='client-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)