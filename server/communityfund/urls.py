from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from communityfund import settings


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include('communityfund.apps.home.urls')),
    url(r'^search/', include('communityfund.apps.search.urls')),
    url(r'^accounts/', include('communityfund.apps.accounts.urls')),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_URL)
urlpatterns += staticfiles_urlpatterns()


