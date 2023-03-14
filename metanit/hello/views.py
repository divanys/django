from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()

    return render(request, 'hello/index.html', {'title': 'главная страница сайта', 'tasks': tasks}) 


def about(request):
    return render(request, 'hello/about.html') 


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Форма была неправильной"

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'hello/create.html', context) 


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страницу съели серые волки какашки</h1>')