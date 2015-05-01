from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'IslamApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
    
    url(r'^quran/api/', include('digital_QURAN.urls')),
)


urlpatterns += staticfiles_urlpatterns()