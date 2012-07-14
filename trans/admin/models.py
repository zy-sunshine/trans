from django.db import models
from django.contrib.auth.models import User as AdminUser
from django.db.models import ForeignKey, CharField, URLField, BooleanField, EmailField, IPAddressField, DateField
class User(models.Model):
	user = ForeignKey(AdminUser)
	ip = IPAddressField()
	site = URLField()

	def __unicode__(self):
		self.user.username

	def __str__(self):
		return self.__unicode__().encode('utf-8')
