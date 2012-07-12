from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
import trans.comments.urls, trans.translations.urls, trans.admin.urls
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'trans.views.Home', name='home'),
    url(r'^book/(?P<book>[^/]*)/$', 'trans.views.BookToc', name='book'),
    url(r'^book/(?P<book>[^/]*)/chapter/(?P<chapterIdx>[^/]*)/$', 'trans.views.Chapter', name='chapter'),
    url(r'^book/(?P<book>[^/]*)/chapter/(?P<chapterIdx>[^/]*)/comments/', include(trans.comments.urls)),
    url(r'^book/(?P<book>[^/]*)/chapter/(?P<chapterIdx>[^/]*)/translations/', include(trans.translations.urls)),
    url(r'^book/(?P<book>[^/]*)/chapter/(?P<chapterIdx>[^/]*)/translate/', 'trans.translations.views.Translate'),
    
    # url(r'^tran/', include('tran.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(trans.admin.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    # MEDIA dirs can store uploaded images, files.  TODO: open it when needed.
    (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.strip('/\\'), 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    (r'^%s/(?P<path>.*)$' % settings.IMAGES_URL.strip('/\\'), 'django.views.static.serve', {'document_root': settings.IMAGES_ROOT, 'show_indexes': True}),
    # STATIC dirs is used as prefix for js css, and set in django.conf.settings
)
