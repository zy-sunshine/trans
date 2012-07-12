from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('trans.translations.views',
    url(r'^counts/$', 'Counts'),
)
