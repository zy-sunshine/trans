from django import forms
from trans.books.models import BookInfo, TocInfo, Lang
from trans.manage.models import User
from django.forms import CharField, DateField, ChoiceField, MultipleChoiceField

class BookInfoForm(forms.ModelForm):
	class Meta:
		model = BookInfo
		fields = ('name' ,'slug', 'link_orig', 'lang_orig_fk', 'description')

# class UserForm(forms.ModelForm):
# 	class Meta:
# 		model = User
# 		fields = ('ip', 'site')

class TocInfoForm(forms.ModelForm):
	para_sep = ChoiceField(label='paragraph separator', 
					choices=(('p', '<p>'),('div', '<div>')),
					initial=('p', 'div'),
				)
	other_sep = MultipleChoiceField(label='other separator', 
					choices=(('pre', '<pre>'), ('blockquote', '<blockquote>'),
						('ul', '<ul>'), ('ol', '<ol>'), ('h1', '<h1>'), ('h2', '<h2>'), ('h3', '<h3>')), 
					widget=forms.CheckboxSelectMultiple(),
					initial=('pre','blockquote', 'ul', 'ol', 'h1', 'h2', 'h3'))
	content = CharField(label = "Toc Content", widget=forms.Textarea(attrs={'cols': 80, 'rows': 20}))
	class Meta:
		model = TocInfo
		fields = ('name', 'slug')

class LangForm(forms.ModelForm):
	class Meta:
		model = Lang
		fields = ('name', )