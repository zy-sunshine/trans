#encoding=utf8
from trans.utils.base import SiteRequestHandler
from trans.manage.forms import BookInfoForm, TocInfoForm, LangForm
#include <stdlib.h>
from trans.manage.models import User
from trans.books.models import Lang, BookInfo, Paragraph_Orig, Paragraph_Trans, TocInfo
from django.template import Template
from django.contrib import auth
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

import logging
log = logging.getLogger('django')
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
        self.render('trans/manage/index.html')

class AddBook(SiteRequestHandler):
    def POST(self):
        form = BookInfoForm(self.request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.instance.user = auth.get_user(self.request)
            log.info(auth.get_user(self.request))
            form.save()
            # fc = {
            #     'lang_orig_fk': self.param('lang_orig_fk'),
            #     'heros': self.paramlist('heros'),
            #     'description': form.cleaned_data['description'], #self.param('description'),
            # }
            # self.write('valid form!! %s' % str(fc))

            self.success('valid form!!')
        else:
            self.render('trans/manage/addbook.html', {'form': form, 'action': '/manage/addbook/'})

    def GET(self):
        form = BookInfoForm()
        context = {'form': form, 'action': '/manage/addbook/'}
        self.render('trans/manage/addbook.html', context)

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
        self.render('trans/manage/editbook.html', {'form': form, 'action': '/manage/editbook/%s/' % slug})

class ListBooks(SiteRequestHandler):
    def GET(self):
        self.render('trans/manage/listbooks.html', {'books': BookInfo.objects.all()})

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
        form = TocInfoForm(self.request.POST)
        form.save(commit=False)
        try:
            bookinfo = BookInfo.objects.get(slug=book)
        except ObjectDoesNotExist:
            self.error(_('Can not find %s book? Please Check!' % book))
            return
        form.instance.bookinfo_fk = bookinfo
        tocinfo = form.save()

        lang_fk = tocinfo.bookinfo_fk.lang_orig_fk

        i = 0
        for elem in results:
            isPara = elem.name == para_sep and True or False
            elem.attrs = ''
            # Clean attrs
            for child in elem.findAll():
                if child.name != 'img':
                    child.attrs = ''
            para = Paragraph_Orig(tocinfo_fk=tocinfo, 
                lang_fk = lang_fk,
                content = str(elem),
                user = auth.get_user(self.request),
                isPara = isPara,
                tag = elem.name,
                order = i,
            )
            para.save()
            i += 1
        self.success('insert %s Paragraph_Orig' % i)

    def GET(self, book=''):
        form = TocInfoForm()
        context = {'form': form, 'action': '/manage/addtoc/book/%s/' % book}
        self.render('trans/manage/addtoc.html', context)

class EditToc(SiteRequestHandler):
    def GET(self, book='', toc=''):
        bookinfo = BookInfo.objects.get(slug=book)
        tocinfo = TocInfo.objects.get(bookinfo_fk=bookinfo, slug=toc)
        para = Paragraph_Orig.objects.filter(tocinfo_fk=tocinfo, lang_fk=bookinfo.lang_orig_fk).order_by('order')
        context = {'para': para}
        self.render('trans/manage/edittoc.html', context)

class DelToc(SiteRequestHandler):
    def GET(self, book='', toc=''):
        bookinfo = BookInfo.objects.get(slug=book)
        tocinfo = TocInfo.objects.get(bookinfo_fk=bookinfo, slug=toc)
        try:
            Paragraph_Trans.objects.filter(tocinfo_fk=tocinfo).delete()
            Paragraph_Orig.objects.filter(tocinfo_fk=tocinfo).delete()
        except:
            self.error('Can not delete toc: %s in book: %s' % (tocinfo.name, bookinfo.name))
        else:
            self.success('Success delete toc: %s in book: %s' % (tocinfo.name, bookinfo.name))
        tocinfo.delete()

# class AddUser(SiteRequestHandler):
#     def POST(self):
#         form = UserForm(self.request.POST)
#         if form.is_valid():
#             fc = {
#                 'username': self.param('username'), 
#                 'nickname': self.param('nickname'),
#                 'ip': '0.0.0.0',
#                 'email': self.param('email'),
#                 'site': self.param('site'),
#                 'ismanage': self.param('ismanage'),
#                 'isAuthor': self.param('isAuthor'),
#                 'datetime': datetime.now(),
#             }
#             u = User(**fc)
#             u.save()
#             self.write('valid form!!\n %s' % str(fc))
#         else:
#             self.render('trans/manage/adduser.html', {'form': form})

#     def GET(self):
#         form = UserForm()
#         context = {'form': form, 'action': '/manage/adduser/'}
#         self.render('trans/manage/adduser.html', context)

class AddLang(SiteRequestHandler):
    def POST(self):
        form = LangForm(self.request.POST)
        if form.is_valid():
            fc = {'name': self.param('name')}
            l = Lang(**fc)
            l.save()
            self.success('valid form! %s' % str(fc))
        else:
            context = {'form': form, 'action': '/manage/addlang/'}
            self.render('trans/manage/addlang.html', context)
    def GET(self):
        form = LangForm()
        context = {'form': form, 'action': '/manage/addlang/'}
        self.render('trans/manage/addlang.html', context)

#from trans.utils.shortcut import register_templatetags
#register_templatetags(['trans.manage.templatetags.base_extras'])
