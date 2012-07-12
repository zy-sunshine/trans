#encoding=utf8
from trans.utils.base import SiteRequestHandler
from trans.admin.forms import BookInfoForm, UserForm
from django.template import Template

class Index(SiteRequestHandler):
	def GET(self):
		self.write('Admin Index Page!')

class AddBook(SiteRequestHandler):
	tpl = Template('''
  <form action="/admin/addbook/" method="POST">
    {% csrf_token %}  
    {% for field in form %}
      <div class="fieldWrapper">
         {{ field.label_tag }}:{{ field }} 
         {{ field.errors }}
      </div>
    {% endfor %}
    <div class="fieldWrapper"><p><input type="submit" value="留言" /></p></div>
  </form>
				''')
	def POST(self):
		form = BookInfoForm(self.request.POST)
		if form.is_valid():
			self.write('valid form!!')
		else:
			self.renderEx(self.tpl, {'form': form})

	def GET(self):
		form = BookInfoForm()
		
		context = {'form': form}
		self.renderEx(self.tpl, context)

class AddUser(SiteRequestHandler):
	tpl = Template('''
  <form action="/admin/adduser/" method="POST">
    {% csrf_token %}  
    {% for field in form %}
      <div class="fieldWrapper">
         {{ field.label_tag }}:{{ field }} 
         {{ field.errors }}
      </div>
    {% endfor %}
    <div class="fieldWrapper"><p><input type="submit" value="留言" /></p></div>
  </form>
				''')
	def POST(self):
		form = UserForm(self.request.POST)
		if form.is_valid():
			self.write('valid form!!')
		else:
			self.renderEx(self.tpl, {'form': form})

	def GET(self):

		form = UserForm()
		
		context = {'form': form}
		self.renderEx(self.tpl, context)