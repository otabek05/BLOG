from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Todo

@login_required(login_url='login')
def index(request):
    
    if request.method == 'POST':
        todo = request.POST.get('todo')
        user = request.user
        
        Todo.objects.create(
            owner=user,
            body=todo
        ).save()
        return redirect('home')

    tasks = Todo.objects.filter(owner=request.user)
    context = {
        'tasks': tasks,
    }
    return render(request, "main/index.html", context)


@login_required(login_url='login')
def complete_todo(request, pk):
    task = Todo.objects.get(id=pk)
    task.completed = True
    task.save()
    return redirect('home')

@login_required(login_url='login')
def delete_todo(request, pk):
    task = Todo.objects.get(id=pk)
    task.delete()
    return redirect('home')




