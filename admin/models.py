from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
	user = models.ForeignKey(User)
	nickname = models.CharField(max_length=50)
	email=models.CharField(max_length=50)
	website = models.TextField()
	isAdmin=models.BooleanField(default=False)
	isAuthor=models.BooleanField(default=True)

	def __unicode__(self):
		if self.nickname:
			return self.nickname
		else:
			return self.user.nickname()

	def __str__(self):
		return self.__unicode__().encode('utf-8')
