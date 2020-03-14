from django.db import models
from django.urls import reverse


# Create your models here.

class Post(models.Model):
	titlu = models.TextField(max_length = 50, blank = False)
	text = models.TextField(blank = False)
	descriere = models.TextField(max_length = 250, blank = False)
	data_publicarii = models.DateField(default = "AAAA-LL-ZZ")
	
	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk':self.pk})
		
class Documente(models.Model):
	text = models.TextField(blank = False)
	doc = models.FileField(upload_to='documente')
	data = models.DateField(auto_now = True)
	
	def __str__(self):
		return self.text

	def get_absolute_url(self):
		return reverse('documente', kwargs={'pk':self.pk})

class Activitati(models.Model):
	data_publicarii = models.DateField(default = "AAAA-LL-ZZ")
	titlu = models.TextField(max_length = 50, blank = False)
	text = models.TextField(blank = False)
	
	def get_absolute_url(self):
		return reverse('activitati', kwargs={'pk':self.pk})

	
class Images(models.Model):
	activitati = models.ForeignKey(Activitati, on_delete = models.CASCADE, default = None)
	image = models.ImageField(upload_to ='images/', blank = True, null = True)

	def __str__ (self):
		return self.post.titlu + 'Image'