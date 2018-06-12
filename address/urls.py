from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import AddressList, AddressDetail, AddressCreate

urlpatterns = [
    url(r'^address/list/$', AddressList.as_view(), name='address-list'),
    url(r'^address/detail/(?P<pk>[1-9]+)/$', AddressDetail.as_view(), name='address-detail'),
    url(r'^address/create/$', AddressCreate.as_view(), name='address-create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)