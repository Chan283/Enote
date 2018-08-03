from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Notes(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	title=models.CharField(max_length=255)
	subject=models.CharField(max_length=255)
	text=models.TextField()
	
	def get_absolute_url(self):
		return reverse('notes_detail',kwargs={'pk':self.pk})