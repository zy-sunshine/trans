from trans.utils.base import SiteRequestHandler

class Counts(SiteRequestHandler):
	def GET(self, book='', chapterIdx=''):
		self.write('[]')

class Translate(SiteRequestHandler):
	def GET(self, book='', chapterIdx=''):
		self.write('''
			<p>Translate Page!</p>
			<p>Translate Page!</p>
			<p>Translate Page!</p>
			<p>Translate Page!</p>
			<p>Translate Page!</p>
			<p>Translate Page!</p>
			<p>Translate Page!</p>
			<p>Translate Page!</p>
			<p>Translate Page!</p>
			<p>Translate Page!</p>
			<p>Translate Page!</p>
			<p>Translate Page!</p>
			<p>Translate Page!</p>
			<p>Translate Page!</p>
			<p>Translate Page!</p>
			<p>Translate Page!</p>
			<p>Translate Page!</p>
			<p>Translate Page!</p>
			<p>Translate Page!</p>
			<p>Translate Page!</p>
			<p>Translate Page!</p>
			<p>Translate Page!</p>
			<p>Translate Page!</p>

			<p>Translate Page!</p>
			<p>Translate Page!</p><p>Translate Page!</p>

			<p id="cn2">cn2</p>
			<p>Translate Page!</p><p>Translate Page!</p>
			<p>Translate Page!</p><p>Translate Page!</p>
			<p>Translate Page!</p><p>Translate Page!</p>
			<p>Translate Page!</p><p>Translate Page!</p>
			<p>Translate Page!</p><p>Translate Page!</p>
			<p>Translate Page!</p><p>Translate Page!</p>
			<p>Translate Page!</p><p>Translate Page!</p>
			<p>Translate Page!</p><p>Translate Page!</p>
			<p>Translate Page!</p><p>Translate Page!</p>
			<p>Translate Page!</p><p>Translate Page!</p>
			<p>Translate Page!</p><p>Translate Page!</p>
			<p>Translate Page!</p><p>Translate Page!</p>
			<p>Translate Page!</p><p>Translate Page!</p>
			<p>Translate Page!</p><p>Translate Page!</p>
			<p>Translate Page!</p><p>Translate Page!</p>
			<p>Translate Page!</p><p>Translate Page!</p>

			''')