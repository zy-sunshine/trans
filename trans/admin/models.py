from django.db import models
from django.contrib.auth.models import User as AdminUser
from django.db.models import ForeignKey, CharField, URLField, BooleanField, EmailField, IPAddressField, DateField
class User(models.Model):
	user = ForeignKey(AdminUser)
	nickname = CharField(max_length=50)
	ip = IPAddressField()
	email = EmailField(max_length=50)
	site = URLField()
	isAdmin = BooleanField(default=False)
	isAuthor = BooleanField(default=True)
	datetime = DateField()

	def __unicode__(self):
		if self.nickname:
			return self.nickname
		else:
			return self.user.nickname()

	def __str__(self):
		return self.__unicode__().encode('utf-8')
