from django.db import models
from trans.admin.models import User
from django.db.models import ForeignKey, TextField, DateField, CharField, EmailField, IPAddressField, URLField
from trans.books.models import TocInfo

class Comments(models.Model):
	tocinfo_fk = ForeignKey(TocInfo)
	name = CharField(max_length=50)
	email = EmailField()
	ip = IPAddressField()
	site = URLField()
	comment = TextField()
	datetime = DateField(auto_now=True)
