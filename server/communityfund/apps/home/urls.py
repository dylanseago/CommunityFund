from django.conf.urls import patterns, url

from communityfund.apps.home import views


urlpatterns = patterns('',
                       url(r'^/?$', views.index, name='index'),
                       url(r'^about/?$', views.index, name='about'),
                       url(r'^projects/?$', views.projects, name='projects'),
                       url(r'^communities/?$', views.communities, name='communities'),
                       url(r'^profile/?$', views.profile, name='profile'),
)


