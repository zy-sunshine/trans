from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('trans.admin.views',
    url(r'^$', 'Index', name='admin_index'),
    url(r'^addbook/$', 'AddBook', name='admin_addbook'),
    url(r'^adduser/$', 'AddUser', name='admin_adduser'),
)
