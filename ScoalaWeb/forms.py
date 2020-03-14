from django import forms
from .models import Documente, Activitati, Images

class DocForm(forms.ModelForm):
	class Meta:
		model = Documente
		fields = ['text', 'doc']


class ActivitatiForm(forms.ModelForm):
	class Meta:
		model = Activitati
		fields = ['titlu', 'text', 'data_publicarii']

class ImageForm(forms.ModelForm):
	image = forms.ImageField(label = 'Image')
	class Meta: 
		model = Images
		fields = ('image',)