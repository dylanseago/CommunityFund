from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from communityfund import settings


admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^', include('home.urls')),
    url(r'^admin/', include(admin.site.urls)),
                       url(r'^search/?$', 'search.views.project_result', name='search'),
                       url(r'^accounts/login/?$', 'django.contrib.auth.views.login', {'template_name': 'login.html'},
                           name='login'),
                       url(r'^accounts/register/?$', 'home.views.index', name='register')
) + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
urlpatterns += staticfiles_urlpatterns()


