from trans.utils.base import SiteRequestHandler
from trans.books.models import BookInfo, TocInfo, Paragraph_Trans, Paragraph_Orig
from django.core.exceptions import ObjectDoesNotExist
import json, simplejson
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

class SaveParagraphs(SiteRequestHandler):
    def POST(self):
    	ret = {}
    	if not self.request.is_ajax():
    		ret['ret'] = False
    	else:
    		dataobj = simplejson.loads(self.request.raw_post_data)
    		try:
	    		for data in dataobj['data']:
	    			#Paragraph_Orig.objects.filter(id=data['id']).update(content=data['content'], order=data['idx'])	# do not use it because io speed.
	    			fchange = False
	    			para = Paragraph_Orig.objects.get(id=data['id'])
	    			if para.content != data['content']:
	    				para.content = data['content']
	    				fchange = True
	    			if para.order != data['idx']:
	    				para.order = data['idx']
	    				fchange = True
	    			if fchange:
	    				para.save()
    		except:
    			ret['ret'] = False
    			ret.setdefault('msg', []).append('save paragraph occur error!')
    		else:
    			ret['ret'] = True
    		try:
    			# pretend me a GET method request to call DelParagraph
    			self.request.method = 'GET'
	    		for id in dataobj['del']:
	    			DelParagraph(self.request, id)
	    			#Paragraph_Orig.objects.filter(id=id).delete()
	    		self.request.method = 'POST'
	    	except:
	    		ret['ret'] = False
	    		ret.setdefault('msg', []).append('save paragraph occur error!')
    		else:
    			ret['ret'] = True
    	self.write(simplejson.dumps(ret))

class InfoParagraph(SiteRequestHandler):
	def get_info(self, para):
		return {'user': str(para.user), 'datetime': str(para.datetime)}
	def GET(self):
		para_id = self.param('para_id')
		ret = {'ret': True, }
		try:
			para_orig = Paragraph_Orig.objects.get(id=para_id)
		except Exception, e:
			ret['ret'] = False
			ret.setdefault('msg', []).append('get objects from Paragraph_Orig error')
		else:
			ret['ret'] = True
			ret['data'] = self.get_info(para_orig)
			for p in Paragraph_Trans.objects.filter(para_orig_fk = para_orig):
				ret['data'].setdefault('trans', []).append(self.get_info(p))
		self.write(simplejson.dumps(ret))
