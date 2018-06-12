from django.conf.urls import url

from django.contrib.auth import views as auth_views

from rest_framework.urlpatterns import format_suffix_patterns

#from accounts.views import UserList, UserDetail, UserCreate
from accounts.api.views import UserCreateAPIView, UserListAPIView, UserDetailAPIView

#from .views import login, search

urlpatterns = [

    #url(r'^l/', login),
    # Users
    # path api/users/
    url('^', auth_views.LoginView.as_view(template_name='registration/login.html')),
#    url('^change-password/$', auth_views.PasswordChangeView.as_view(template_name='change-password.html'))

]





urlpatterns = format_suffix_patterns(urlpatterns)