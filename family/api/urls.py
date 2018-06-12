from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from family.api.views import GeneralFamilyView, GeneralFamilyDetail

urlpatterns = [
    # Family
    # path api/family/
    url(r'^list/$', GeneralFamilyView.as_view(), name='family-list'), #GET
    #url(r'^create/$', UserCreateAPIView.as_view(), name='client-create'), #POST
    url(r'^detail/(?P<pk>[0-9]+)/$', GeneralFamilyDetail.as_view(), name='client-detail') #GET, PUT and DELETE
]

urlpatterns = format_suffix_patterns(urlpatterns)