from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns('',
   url(r'^/?$', views.index, name='index'),
   url(r'^about/?$', views.index, name='about'),
   url(r'^projects/?$', views.projects, name='projects'),
   url(r'^communities/?$', views.communities, name='communities'),
   url(r'^profile/?$', views.profile, name='profile'),
   url(r'^c/(?P<community_id>\d+)/?', views.community, name='community'),
   url(r'^p/(?P<project_id>\d+)/?', views.project, name='project'),
   url(r'^u/(?P<user_id>\d+)/?', views.user, name='user'),
)


