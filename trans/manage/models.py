from django.db import models
from django.contrib.auth.models import User
from django.db.models import ForeignKey, CharField, URLField, BooleanField, EmailField, IPAddressField, DateField
class UserProfile(models.Model):
	user = ForeignKey(User)
	ip = IPAddressField()
	site = URLField()

	def __unicode__(self):
		return self.user.username

	def __str__(self):
		return self.__unicode__().encode('utf-8')
