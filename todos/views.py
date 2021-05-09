# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
# Create your views here.

def index(request):
	todos = Todo.objects.all()[:10] #requesting 10 todo objects from Todo Model
	context = {
		'todos': todos
	}
	# Todo.objects.get(id='3').delete();

	return render(request, 'index.html', context)

def details(request, id):
	todo = Todo.objects.get(id=id)
	context = {
	'todo': todo
	}
	return render(request, 'details.html', context)

def remove(request, id):
	Todo.objects.get(id=id).delete();
	return redirect('/todos')

def add(request):
	if(request.method == 'POST'):
		title = request.POST['title']
		text = request.POST['text']

		todo = Todo(title=title, text=text)
		todo.save()
		return redirect('/todos')
	else:
		return render(request, 'add.html')

def edit(request,id):
	todo = Todo.objects.get(id=id)
	context = {
		'todo': todo
	}
	if(request.method == 'POST'):
		id = id
		title = request.POST['title']
		text = request.POST['text']
		Todo.objects.filter(id=id).update(title=title,text=text)
		return redirect('/todos')
	else:
		return render(request, 'edit.html', context)