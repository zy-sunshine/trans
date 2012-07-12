from django.db import models
from trans.admin.models import User
from django.db.models import ForeignKey, TextField, DateField, CharField, ManyToManyField
from django.db.models import EmailField, IPAddressField, URLField

class BookInfo(models.Model):
	user = User()
	link_orig = URLField()
	name = CharField(max_length=200)
	lang_orig_fk = ForeignKey('Lang')
	heros = ManyToManyField(User)
	description = TextField()
	datetime = DateField(auto_now=True)

class Lang(models.Model):
	name = CharField(max_length=50)

class TocInfo(models.Model):
	bookinfo_fk = ForeignKey('BookInfo')
	name = CharField(max_length=100)
	
class Toc(models.Model):
	tocinfo_fk = ForeignKey('TocInfo')
	lang_fk = ForeignKey('Lang')
	content = TextField()
	user = User()
	message = CharField(max_length=100)
	datetime = DateField(auto_now=True)
	
# class Comments(models.Model):
# 	tocinfo_fk = ForeignKey('TocInfo')
# 	name = CharField(max_length=50)
# 	email = EmailField()
# 	ip = IPAddressField()
# 	site = URLField()
# 	comment = TextField()
# 	datetime = DateField(auto_now=True)
