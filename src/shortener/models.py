from django.db import models

# Create your models here.

class KirrURL(models.Model):
	url = models.CharField(max_length=220, )
	shortcode = models.CharField(max_length=15, null=True, unique=True)

	def __str__(self):
		return (self.url)

