from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'trans.views.Home', name='home'),
    url(r'^book/(?P<book>.*)/chapter/(?P<idx>.*)$', 'trans.views.Chapter', name='chapter'),
    # url(r'^tran/', include('tran.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    # MEDIA dirs can store uploaded images, files.  TODO: open it when needed.
    #(r'^%s/(?P<path>.*)$' % MEDIA_URL.strip('/\\'), 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    # STATIC dirs is used as prefix for js css, and set in django.conf.settings
)
