from django.db import models
from django.contrib.auth.models import User
from django.db.models import ForeignKey, TextField, DateTimeField, CharField, ManyToManyField
from django.db.models import EmailField, IPAddressField, URLField, SlugField, BooleanField, IntegerField
from django.utils.translation import ugettext_lazy as _

class BookInfo(models.Model):
	user = ForeignKey(User)
	link_orig = URLField()
	name = CharField(max_length=200)
	slug = SlugField(unique=True)
	lang_orig_fk = ForeignKey('Lang', verbose_name=_('Lang orig'))
	description = TextField()
	datetime = DateTimeField(auto_now=True)

class Lang(models.Model):
	name = CharField(max_length=50, unique=True)
	def __unicode__(self):
		return self.name

class TocInfo(models.Model):
	bookinfo_fk = ForeignKey('BookInfo', verbose_name=_('Book Belong'))
	name = CharField(max_length=100, verbose_name=_('Toc Name'))
	slug = SlugField(unique=True)

class Paragraph(models.Model):
	tocinfo_fk = ForeignKey('TocInfo', verbose_name=_('Toc Belong'))
	lang_fk = ForeignKey('Lang', verbose_name=_('Paragraph Lang'))
	content = TextField()
	user = ForeignKey(User, verbose_name=_('Hero User'))
	isPara = BooleanField(verbose_name=_('Is Paragraph Node?'))
	tag = CharField(max_length=20, verbose_name=_('Html Tag'))
	message = CharField(max_length=100, verbose_name=_('Commit Message'))
	order = IntegerField()
	datetime = DateTimeField(auto_now=True)
	class Meta:
		abstract = True

class Paragraph_Orig(Paragraph):
	pass

class Paragraph_Trans(Paragraph):
	para_orig_fk = ForeignKey(Paragraph_Orig, related_name='trans')

# class Comments(models.Model):
# 	tocinfo_fk = ForeignKey('TocInfo')
# 	name = CharField(max_length=50)
# 	email = EmailField()
# 	ip = IPAddressField()
# 	site = URLField()
# 	comment = TextField()
# 	datetime = DateTimeField(auto_now=True)
