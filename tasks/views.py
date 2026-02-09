from django.shortcuts import render,get_object_or_404, redirect

from .models import Task
# Create your views here.

def task_list(request):
    tasks= Task.objects.all().order_by('-created_date')
    return render(request, 'tasks/task_list.html', {'tasks':tasks})

def add_task(request):
    if request.method =='POST':
        title =request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request,'tasks/add_task.html')

def complete_task(request,task_id):
    task = get_object_or_404(Task, id= task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

def delete_task(request, task_id):
    task = get_object_or_404(Task, id =task_id)
    task.delete()
    return redirect('task_list')