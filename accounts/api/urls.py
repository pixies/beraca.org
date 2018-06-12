from django.conf.urls import url

from django.contrib.auth import views as auth_views

from rest_framework.urlpatterns import format_suffix_patterns

#from accounts.views import UserList, UserDetail, UserCreate
from accounts.api.views import UserCreateAPIView, UserListAPIView, UserDetailAPIView

urlpatterns = [
    # Users
    # path api/users/
    url(r'^list/$', UserListAPIView.as_view(), name='client-list'),
    url(r'^create/$', UserCreateAPIView.as_view(), name='client-create'),
    url(r'^detail/(?P<pk>[0-9]+)/$', UserDetailAPIView.as_view(), name='client-detail'),

    #url('^login/$', auth_views.LoginView.as_view()),
    #url('^change-password/$', auth_views.PasswordChangeView.as_view(template_name='change-password.html'))

]





urlpatterns = format_suffix_patterns(urlpatterns)