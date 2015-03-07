from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
   url(r'^/?$', views.index, name='index'),
   url(r'^about/?$', views.about, name='about'),
   url(r'^projects/?$', views.projects, name='projects'),
   url(r'^communities/?$', views.communities, name='communities'),

   url(r'^p/create/?$', views.create_project, name='create_project'),
   url(r'^c/create/?$', views.create_community, name="create_community"),

   url(r'^u/(?P<user_id>\d+)/?', views.user, name='user'),
   url(r'^p/(?P<project_id>\d+)/?', views.project, name='project'),
   url(r'^c/(?P<community_id>\d+)/?', views.community, name='community'),
)


