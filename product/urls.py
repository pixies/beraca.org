from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import ProductList, ProductDetail, ProductCreate, ProductUpdate

urlpatterns = [
    url(r'^list/$', ProductList.as_view(), name='product-list'),
    url(r'^create/$', ProductCreate.as_view(), name='product-create'),
    url(r'^update/(?P<pk>[0-9]+)/$', ProductUpdate.as_view(), name='product-update'),
    url(r'^detail/(?P<pk>[0-9]+)/$', ProductDetail.as_view(), name='product-detail')
]

urlpatterns = format_suffix_patterns(urlpatterns)