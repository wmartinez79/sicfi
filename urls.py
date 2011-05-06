from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.defaults import *
from django.views.static import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'sicfi.views.index'),
    (r'^catalogos/', include('sicfi.catalogos.urls')),
    (r'^configuracion/', include('sicfi.configuracion.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
    # Examples:
    # url(r'^$', 'sicfi.views.home', name='home'),
    # url(r'^sicfi/', include('sicfi.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^headers/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_HEADERS_ROOT}),
        (r'^images/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_IMAGES_ROOT})
    )