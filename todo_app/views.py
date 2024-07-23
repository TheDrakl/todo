from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm, TaskHomeForm
from django.contrib import messages
from .models import Task

def home(request):
    if request.method == 'POST':
        form = TaskHomeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task created successfully')
            return redirect('home')
    else:
        form = TaskHomeForm()

    tasks = Task.objects.all()
    context = {
        'form': form,
        'tasks': tasks
    }
    return render(request, 'todo_app/home.html', context)




def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task created successfully!")
            return redirect('home')
    else:
            form = TaskForm()
    return render(request, 'todo_app/create_task.html', {'form': form})

def update(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = True
    task.save()
    return redirect('home')

def update_not_completed(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.is_completed = False
    task.save()
    return redirect('home')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')

def details(request,task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'todo_app/details.html', {'task': task}) 