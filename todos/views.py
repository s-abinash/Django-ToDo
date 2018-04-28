# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo

# Create your views here.

def index(request):
	todos = Todo.objects.all()[:10] #requesting 10 todo objects from Todo Model
	context = {
		'todos': todos
	}
	return render(request, 'index.html', context)
