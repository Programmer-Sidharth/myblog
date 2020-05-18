from django.contrib.auth import get_user_model
from django import forms
from .models import *
class BlogPostForm(forms.Form):
	title = forms.CharField()
	slug = forms.SlugField()
	message = forms.CharField(widget=forms.Textarea)
	published = forms.DateTimeField()

class BlogPostModelForm(forms.ModelForm):
	class Meta:
		model = BlogPost
		fields = ['title', 'slug', 'message']

class LoginForm(forms.ModelForm):
	class Meta:
		model = get_user_model()
		fields = ['username', 'password']

		