from trans.utils.base import SiteRequestHandler
from trans.books.models import BookInfo, TocInfo, Paragraph_Trans, Paragraph_Orig
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
		[{'name': 'namestr', 'slug': 'slugstr'}]
		if tocs:
			ajax_str = '['
			for toc in tocs:
				ajax_str += '{"name": "%s", "slug": "%s"},' % (toc.name, toc.slug)
				Log.info(toc)
			ajax_str = ajax_str.rstrip(',') + ']'
		else:
			ajax_str = '[]'
		self.write(ajax_str)

class DelParagraph(SiteRequestHandler):
	def GET(self, para_id=None):
		if para_id is not None:
			para_orig = Paragraph_Orig.objects.get(id=para_id)
			para_trans = Paragraph_Trans.objects.filter(para_orig_fk=para_orig)
			if para_trans:
				para_trans.delete()
			para_orig.delete()
