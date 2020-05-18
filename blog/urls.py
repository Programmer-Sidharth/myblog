from django.urls import path
from .views import *

urlpatterns = [
	path('', home, name='blog'),
	path('<str:slug>/', blogpost),
	path('<str:slug>/delete/', delete),
	path('<str:slug>/edit/', edit),
]