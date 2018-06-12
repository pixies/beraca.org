from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import CompanyList, CompanyDetail

urlpatterns = [
    url(r'^company/list/$', CompanyList.as_view(), name='company-list'),
    url(r'^company/create/$', CompanyList.as_view(), name='company-create'),
    url(r'^company/detail/(?P<pk>[0-9]+)/$', CompanyDetail.as_view(), name='company-detail'),
    url(r'^company/update/(?P<pk>[0-9]+)/$', CompanyDetail.as_view(), name='company-update')
]

urlpatterns = format_suffix_patterns(urlpatterns)
