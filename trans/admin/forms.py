from django import forms
from trans.books.models import BookInfo, TocInfo, Lang
from trans.admin.models import User
from django.forms import CharField, DateField

class BookInfoForm(forms.ModelForm):
	class Meta:
		model = BookInfo
		fields = ('name' ,'slug', 'link_orig', 'lang_orig_fk', 'description')

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'nickname', 'email', 'site', 'isAdmin', 'isAuthor')

class TocInfoForm(forms.ModelForm):
	content = CharField(label = "Toc Content", widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))
	class Meta:
		model = TocInfo
		fields = ('name', )

class LangForm(forms.ModelForm):
	class Meta:
		model = Lang
		fields = ('name', )