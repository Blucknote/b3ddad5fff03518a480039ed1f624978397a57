from django.db import models
from datetime import datetime

class chart_row(models.Model):
	func = models.TextField()
	chart = models.ImageField(blank = True, null = True)
	period = models.CharField(max_length=2)
	dt = models.CharField(max_length=2)
	pub_date = models.TextField(blank = True)

	def chart_add(self):
		self.pub_date = datetime.now()
		self.save()
	
	def __str__(self):
		return self.func
# Create your models here.
