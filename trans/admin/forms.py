from django import forms
from trans.books.models import BookInfo
from trans.admin.models import User

class BookInfoForm(forms.ModelForm):
	class Meta:
		model = BookInfo
		fields = ('lang_orig_fk', 'heros', 'description')

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('nickname', 'email', 'site', 'isAdmin', 'isAuthor')
