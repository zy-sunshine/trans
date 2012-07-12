from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('trans.comments.views',
    url(r'^$', 'AjaxComments'),
    url(r'^counts/$', 'Counts'),
    url(r'^(?P<commentIdx>\d*)/$', 'AjaxComment'),
)
