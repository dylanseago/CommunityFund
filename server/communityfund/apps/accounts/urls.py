from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    # TODO: Fix these temporary mappings
    url(r'^login/?$', 'django.contrib.auth.views.login', name='login', kwargs={
        'template_name': 'accounts/login.html'
    }),
    url(r'^logout/?$', 'django.contrib.auth.views.logout', name='logout', kwargs={
        'next_page': 'login',
    }),
    url(r'^signup/?$', 'django.contrib.auth.views.login', name='signup', kwargs={
        'template_name': 'accounts/signup.html'
    }),
    url(r'^profile/?$', views.profile, name='profile'),
)


