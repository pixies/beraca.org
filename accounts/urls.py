from django.conf.urls import url

from django.contrib.auth import views as auth_views

from rest_framework.urlpatterns import format_suffix_patterns

#from accounts.views import UserList, UserDetail, UserCreate
from accounts.api.views import UserCreateAPIView, UserListAPIView, UserDetailAPIView

from .views import login, profile

app_name = 'accounts'

urlpatterns = [

    #url(r'^l/', login),
    # Users
    # path api/users/
    url(r'^profile/$', profile),
    #url('^login/$', login, name='login')
    url(r'^login/$', auth_views.LoginView.as_view(template_name='registration/login.html')),
    url(r'^logout/$', auth_views.LogoutView.as_view()),  # API Auth - URLs
#    url('^change-password/$', auth_views.PasswordChangeView.as_view(template_name='change-password.html'))

]





urlpatterns = format_suffix_patterns(urlpatterns)