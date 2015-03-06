from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # TODO: Fix these temporary mappings
    url(r'^login/?$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^register/?$', 'django.contrib.auth.views.login', {'template_name': 'accounts/register.html'}, name='register')
)


