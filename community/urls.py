from django.conf.urls import url

from rest_framework.urlpatterns import format_suffix_patterns

from .views import CommunityList, CommunityDetail, CommunityCreate, CommunityUpdate

urlpatterns = [
    url(r'^community/create/$', CommunityCreate.as_view(), name='community-create'),
    url(r'^community/list/$', CommunityList.as_view(), name='community-list'),
    url(r'^community/update/(?P<pk>[0-9]+)$', CommunityUpdate.as_view(), name='community-update'),
    url(r'^community/detail/(?P<pk>[0-9]+)/$', CommunityDetail.as_view(), name='community-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)