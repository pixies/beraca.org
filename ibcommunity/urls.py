"""
ibcommunity URL Configuration
"""
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from django.contrib.auth import views as auth_views



urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api/user/', include('accounts.api.urls', namespace='accounts')), #API for Users - URLs
    url(r'^api/client/', include('client.api.urls', namespace='client')),  # API for Users - URLs
    url(r'^api/project/', include('project.urls', namespace='project')),
    url(r'^', include('company.urls', namespace='company')),
    url(r'^', include('address.urls', namespace='address')),
    url(r'^api/product/', include('product.urls', namespace='product')),
    url(r'^', include('community.urls', namespace='community')),
    url(r'^', include('providers.urls', namespace='providers')),
    url(r'^api/family/', include('family.api.urls', namespace='family')),
    url(r'^api/auth/', include('ibcommunity.api.urls')), # API Auth - URLs

    url(r'^index/', include('client.urls')), # API Auth - URLs
    #url(r'^', include('client.urls')), # API Auth - URLs


    #url(r'^index/login/', auth_views.LoginView.as_view(template_name='registration/login.html')),  # API Auth - URLs
    url(r'^accounts/', include('accounts.urls', namespace='accounts'))
    #url(r'^index/logout/', auth_views.LogoutView.as_view()),  # API Auth - URLs
    #url(r'^index/client/', include('client.urls')),  # API Auth - URLs

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
