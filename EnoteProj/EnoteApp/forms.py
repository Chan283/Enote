from django.contrib.auth.models import User
from django import forms
from EnoteApp.models import Notes

class NotesCreateForm(forms.ModelForm):
	class Meta:
		model=Notes
		fields=('title','subject','text')
		
class NotesUpdateForm(forms.ModelForm):
	class Meta:
		model=Notes
		fields=('title','subject','text')

