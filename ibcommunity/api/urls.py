"""
    API Reference - Auth ibcommunity URL Configuration
"""
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    url(r'^$/', include('djoser.urls')),
    url(r'^$/', include('djoser.urls.jwt')),
    url(r'^token/', obtain_jwt_token),
    url(r'^refresh-token/', refresh_jwt_token),
    url(r'^verify-token/', verify_jwt_token),
]
