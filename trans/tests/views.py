from trans.utils.base import SiteRequestHandler

class Message(SiteRequestHandler):
	def GET(self):
		self.render('message.html', {'error': 'error message', 'success': 'success message', 
			'warning': 'warning message', 'info': 'info message'})
		

class Model(SiteRequestHandler):
    def GET(self):
        self.render('tests/t-model.html')
