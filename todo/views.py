from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from .models import Todo


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user_id_id=request.user.id)
        context = {'todos': todos}
        return render(request, 'index.html', context)
    return redirect('login')


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect!')

    context = {}
    return render(request, 'login.html')


def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')


def new_todo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            title = request.POST.get('title')
            user_id = request.user.id
            todo = Todo.objects.create(title=title, user_id_id=user_id)
            return redirect(request.META.get('HTTP_REFERER'))
    return redirect('login')


def done_todo(request, pk):
    if request.user.is_authenticated:
        todo = Todo.objects.get(id=pk)
        if todo.done:
            todo.done = False
        else:
            todo.done = True
        todo.save()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('login')


def delete_todo(request, pk):
    if request.user.is_authenticated:
        todo = Todo.objects.get(id=pk)
        todo.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    return redirect('login')
