from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProviderListView


urlpatterns = [
    url(r'providers/list/$', ProviderListView.as_view(), name='providers_list')
]

urlpatterns = format_suffix_patterns(urlpatterns)