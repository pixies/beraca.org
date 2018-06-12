from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ProjectList, ProjectDetail, ProjectUpdate, ProjectCreate, \
                   ProjectCategoryList, ProjectCategoryCreate, ProjectCategoryDetail, \
                   ProjectCategoryUpdate, ProjectSupportCreate, ProjectSupportList, ProjectSupportDetail


urlpatterns = [
    # Projects
    url(r'^list/$', ProjectList.as_view(), name='project-list'),
    url(r'^create/$', ProjectCreate.as_view(), name='project-create'),
    url(r'^update/(?P<pk>[0-9]+)/$', ProjectUpdate.as_view(), name='project-update'),
    url(r'^detail/(?P<pk>[0-9]+)/$', ProjectDetail.as_view(), name='project-detail'),

    # Project Categories
    url(r'^category/list/$', ProjectCategoryList.as_view(), name='category-list'),
    url(r'^category/create/$', ProjectCategoryCreate.as_view(), name='category-create'),
    url(r'^category/detail/(?P<pk>[0-9]+)/$', ProjectCategoryDetail.as_view(), name='category-detail'),
    url(r'^category/update/(?P<pk>[0-9]+)/$', ProjectCategoryUpdate.as_view(), name='category-update'),

    #API FOR support project
    url(r'^support/create/$', ProjectSupportCreate.as_view(), name='project-support-create'),
    url(r'^support/list/$', ProjectSupportList.as_view(), name='project-support-list'),
    url(r'^support/detail/(?P<pk>[0-9]+)/$', ProjectSupportDetail.as_view(), name='project-support-detail'),


]

urlpatterns = format_suffix_patterns(urlpatterns)