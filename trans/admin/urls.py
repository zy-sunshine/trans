from django.conf.urls import patterns, include, url
from django.conf import settings

urlpatterns = patterns('trans.admin.views',
    url(r'^$', 'Index', name='admin_index'),
    url(r'^addbook/$', 'AddBook', name='admin_addbook'),
    url(r'^adduser/$', 'AddUser', name='admin_adduser'),
    url(r'^addtoc/book/(?P<book>[^/]*)/$', 'AddToc', name='admin_addtoc'),
    url(r'^addlang/$', 'AddLang', name='admin_addlang'),

	url(r'^listbooks/$', 'ListBooks', name='admin_listbooks'),
    url(r'^editbook/(?P<slug>[^/]*)/$', 'EditBook', name='admin_editbook'),
)
urlpatterns += patterns('trans.admin.ajax',
	url(r'^check/book_slug_unique/$', 'BookSlugUnique'),
	url(r'^ajax/get_toclist/$', 'GetToclist')
)
urlpatterns += patterns('trans.admin.authviews',
	url(r'^login/$', 'Login', name='admin_login'),
	)
