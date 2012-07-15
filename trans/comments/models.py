from django.db import models
from django.db.models import ForeignKey, TextField, DateTimeField, CharField, EmailField, IPAddressField, URLField
from trans.books.models import TocInfo

class Comments(models.Model):
	tocinfo_fk = ForeignKey(TocInfo)
	name = CharField(max_length=50)
	email = EmailField()
	ip = IPAddressField()
	site = URLField()
	comment = TextField()
	datetime = DateTimeField(auto_now=True)
