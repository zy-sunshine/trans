from trans.utils.base import SiteRequestHandler
from trans.books.models import BookInfo
from django.core.exceptions import ObjectDoesNotExist
import logging
Log = logging.getLogger('django')

class bookSlugUnique(SiteRequestHandler):
	def GET(self):
		ret = False
		try:
			BookInfo.objects.get(slug = self.param('slug'))
		except ObjectDoesNotExist:
			ret = True
		Log.info('check result %s' % ret)
		self.write('{"ret": %s}' % (ret and 'true' or 'false', ))