#encoding=utf8
from trans.utils.base import SiteRequestHandler
from trans.admin.forms import BookInfoForm, UserForm, TocInfoForm, LangForm
from trans.admin.models import User
from trans.books.models import Lang, BookInfo
from django.template import Template
from datetime import datetime

tpl = Template('''
	{{ ext_var }}
  <form action="{{ action }}" method="POST">
    {% csrf_token %}  
    {% for field in form %}
      <div class="fieldWrapper">
         {{ field.label_tag }}:{{ field }} 
         {{ field.errors }}
      </div>
    {% endfor %}
    <div class="fieldWrapper"><p><input type="submit" value="Submit" /></p></div>
  </form>
				''')

class Index(SiteRequestHandler):
	def GET(self):
		from django.contrib import messages
		messages.error(self.request, 'Campaign you tried to register for, doesn\'t exist.')
		self.render('trans/admin/index.html')

class AddBook(SiteRequestHandler):
	def POST(self):
		form = BookInfoForm(self.request.POST)
		if form.is_valid():
			form.save()
			# fc = {
			# 	'lang_orig_fk': self.param('lang_orig_fk'),
			# 	'heros': self.paramlist('heros'),
			# 	'description': form.cleaned_data['description'], #self.param('description'),
			# }
			# self.write('valid form!! %s' % str(fc))
			self.write('valid form!!')
		else:
			self.render('trans/admin/addbook.html', {'form': form, 'action': '/admin/addbook/'})

	def GET(self):
		form = BookInfoForm()
		context = {'form': form, 'action': '/admin/addbook/'}
		self.render('trans/admin/addbook.html', context)

class EditBook(SiteRequestHandler):
	def POST(self, slug='testslug'):
		form = BookInfoForm(self.request.POST, instance=BookInfo.objects.get(slug=slug))
		if form.is_valid():
			form.save()
			self.write('valid form!! saved success!')
		else:
			self.renderWithSlug(slug)

	def GET(self, slug='testslug'):
		self.renderWithSlug(slug)

	def renderWithSlug(self, slug):
		form = BookInfoForm(instance=BookInfo.objects.get(slug=slug))
		self.render('trans/admin/editbook.html', {'form': form, 'action': '/admin/editbook/%s/' % slug})

class ListBooks(SiteRequestHandler):
	def GET(self):
		self.render('trans/admin/listbooks.html', {'books': BookInfo.objects.all()})

class AddToc(SiteRequestHandler):
	def POST(self, book=''):
		from BeautifulSoup import BeautifulSoup
		name = self.param('name')
		content = self.param('content')
		para_sep = self.param('para_sep')
		other_sep = self.paramlist('other_sep')
		seps = other_sep[:]
		seps.append(para_sep)
		soup = BeautifulSoup(content)
		results = soup.findAll(seps)
		for elem in results:
			if elem.name == para_sep:
				pass
				# this is a text paragraph
			else:
				pass
				# this is another
		self.write(results)

	def GET(self, book=''):
		form = TocInfoForm()
		context = {'form': form, 'action': '/admin/addtoc/book/%s/' % book}
		self.render('trans/admin/addtoc.html', context)

class AddUser(SiteRequestHandler):

	def POST(self):
		form = UserForm(self.request.POST)
		if form.is_valid():
			fc = {
				'username': self.param('username'), 
				'nickname': self.param('nickname'),
				'ip': '0.0.0.0',
				'email': self.param('email'),
				'site': self.param('site'),
				'isAdmin': self.param('isAdmin'),
				'isAuthor': self.param('isAuthor'),
				'datetime': datetime.now(),
			}
			u = User(**fc)
			u.save()
			self.write('valid form!!\n %s' % str(fc))
		else:
			self.render('trans/admin/adduser.html', {'form': form})

	def GET(self):
		form = UserForm()
		context = {'form': form, 'action': '/admin/adduser/'}
		self.render('trans/admin/adduser.html', context)

class AddLang(SiteRequestHandler):
	def POST(self):
		form = LangForm(self.request.POST)
		if form.is_valid():
			fc = {'name': self.param('name')}
			l = Lang(**fc)
			l.save()
			self.write('valid form! %s' % str(fc))
		else:
			self.write('invalid form!!')
	def GET(self):
		form = LangForm()
		context = {'form': form, 'action': '/admin/addlang/'}
		self.render('trans/admin/addlang.html', context)

#from trans.utils.shortcut import register_templatetags
#register_templatetags(['trans.admin.templatetags.base_extras'])
