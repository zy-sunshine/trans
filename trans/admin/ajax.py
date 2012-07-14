from trans.utils.base import SiteRequestHandler
from trans.books.models import BookInfo, TocInfo
from django.core.exceptions import ObjectDoesNotExist
import logging
Log = logging.getLogger('django')

class BookSlugUnique(SiteRequestHandler):
	def GET(self):
		ret = False
		slug = self.param('slug')
		try:
			BookInfo.objects.get(slug = slug)
		except ObjectDoesNotExist:
			ret = True
		Log.info('check result %s, %s' % (ret, slug))
		self.write('{"ret": %s}' % (ret and 'true' or 'false', ))


class GetToclist(SiteRequestHandler):
	def GET(self):
		slug = self.param('slug')
		book = BookInfo.objects.get(slug = slug)
		ajax_str = ''
		tocs = TocInfo.objects.filter(bookinfo_fk = book)
		if tocs:
			ajax_str = '['
			for toc in tocs:
				ajax_str += '"%s",' % toc
				Log.info(toc)
			ajax_str = ajax_str.rstrip(',') + ']'
		else:
			ajax_str = '[]'
		self.write(ajax_str)

