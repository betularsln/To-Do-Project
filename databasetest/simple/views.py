from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
from .forms import ListForm

# Create your views here.

def index(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            todo_list = Todo.objects.all()
            return render(request,"simple/index.html",{'todo_list':todo_list})
    else:
        todo_list = Todo.objects.all()
        return render(request,"simple/index.html",{'todo_list':todo_list})

def about(request):
    return render(request,"simple/about.html")

def create(request):
    if request.method == "POST":
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            todo_list = Todo.objects.all()
            return render(request,"simple/create.html",{'todo_list':todo_list})
    else:
        todo_list = Todo.objects.all()
        return render(request,"simple/create.html",{'todo_list':todo_list})

def delete(request,Todo_id):
    todo = Todo.objects.get(pk=Todo_id)
    todo.delete()
    return redirect("index")

def yes_finish(request,Todo_id):
    todo = Todo.objects.get(pk=Todo_id)
    todo.finished = False
    todo.save()
    return redirect("index")

def no_finish(request,Todo_id):
    todo = Todo.objects.get(pk=Todo_id)
    todo.finished = True  
    todo.save()
    return redirect("index")

def update(request,Todo_id):
    if request.method == "POST":
        todo_list = Todo.objects.get(pk=Todo_id)
        form = ListForm(request.POST or None,instance=todo_list)
        if form.is_valid:
            form.save()
            return redirect("index")
    else:
        todo_list = Todo.objects.all()
        return render(request,"simple/update.html",{'todo_list':todo_list})
    
    