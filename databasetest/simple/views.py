from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Todo
from .forms import ListForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

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


def user_login(request):    	
    if request.method == 'POST':
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')
    
        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)
    
        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                # login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect('index')
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")
    
    else:
        #Nothing has been provided for username or password.
        return render(request, 'simple/login.html', {})
