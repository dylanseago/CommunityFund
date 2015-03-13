from django.conf.urls import patterns, url
from communityfund.apps.home import views


urlpatterns = patterns('',
   url(r'^/?$', views.index, name='index'),
   url(r'^about/?$', views.about, name='about'),
   url(r'^projects/?$', views.projects, name='projects'),
   url(r'^communities/?$', views.communities, name='communities'),

   url(r'^project/create/?$', views.create_project, name='create_project'),
   url(r'^community/create/?$', views.create_community, name="create_community"),

   url(r'^user/(?P<user_id>\d+)/?', views.user, name='user'),
   url(r'^project/(?P<project_id>\d+)/?', views.project, name='project'),
   url(r'^community/(?P<community_id>\d+)/?', views.community, name='community'),
)


