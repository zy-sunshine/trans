from django.conf.urls import patterns, include, url


urlpatterns = patterns('trans.tests.views',
    (r'^message/$', 'Message'),
    (r'^model/$', 'Model'),
)
