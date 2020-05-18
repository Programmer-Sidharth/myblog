from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
import datetime
from django.contrib import messages
from django.contrib.auth import *
from django.contrib import auth as auth_view

# Create your views here.
def home(request):
	post = BlogPost.objects.all()
	context = {'posts':post, 'title':'Posts'}
	return render(request, 'blog-home.html', context)

def blogpost(request, slug):
	post = BlogPost.objects.get(slug=slug)
	context = {'post':post, 'title':post.title}
	return render(request, 'blogpost.html', context)

def login(request):
	return render(request, 'login.html')


def logout(request):
	logout(request)
	return redirect('/blog')

def register(request):
	pass

def post_blog(request):
	form = BlogPostModelForm(request.POST or None)
	if form.is_valid():
		dt = datetime.datetime.now()
		BlogPost.objects.create(author=request.user, **form.cleaned_data, published=dt)
		# BlogPost.objects.create(author=request.user, **form.cleaned_data)
		form = BlogPostModelForm()
	context = {'title':'Post New Blog', 'form':form}
	return render(request, 'post_your_blog.html', context)

def delete(request, slug):
	obj = BlogPost.objects.get(slug=slug)
	if request.method == 'POST':
		title = obj.title
		obj.delete()
		messages.info(request, f'Blogpost "{title}" deleted successfully')
		return redirect('/blog')
	context = {'post':obj, 'title':'delete'}
	return render(request, 'delete.html', context)

def edit(request, slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	form = BlogPostModelForm(request.POST or None, instance=obj)
	if form.is_valid():
		title = obj.title
		form.save()
		form = BlogPostModelForm()
		messages.info(request, f'Blogpost "{title}" is edited successfully')
		return redirect('/blog')
	context = {'title':'edit', 'form':form}
	return render(request, 'edit.html', context)


def search(request):
	topic = request.GET.get('q')
	title = BlogPost.objects.filter(title__icontains=topic)
	message = BlogPost.objects.filter(message__icontains=topic)
	posts = set(title | message)
	context = {
		'title':'search',
		'posts':posts
	}
	return render(request, 'search.html', context)