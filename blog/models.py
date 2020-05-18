from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class BlogPost(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	title = models.CharField(max_length=100, null=True, blank=True)
	slug = models.SlugField(max_length=100, unique=True)
	message = models.TextField(null=True, blank=True)
	published = models.DateTimeField(null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"{self.title} by {self.author.first_name}"