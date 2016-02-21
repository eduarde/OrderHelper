from django.db import models
from django.utils import timezone

class Status(models.Model):
	text = models.CharField(max_length=200)

	def save_status(self):
		self.save()

	def __str__(self):
		return self.text