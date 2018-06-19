from django.db import models
from django.utils import timezone

class chart_row(models.Model):
	func = models.TextField()
	chart = models.ImageField(blank=True, null=True)
	period = models.CharField(max_length=2)
	dt = models.CharField(max_length=2)
	published_date = models.DateTimeField(
            blank=True, null=True)

	def chart_add(self):
		self.published_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.func
# Create your models here.
