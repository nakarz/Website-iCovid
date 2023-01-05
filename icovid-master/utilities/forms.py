from django.forms import ModelForm
from django import forms
from .models import Announcement as AnnouncementModel

class AnnouncementForm(ModelForm):
	class Meta:
		model = AnnouncementModel
		fields = ['title','message']
		
		