from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Tasks
from .forms import TaskForm
# Continue from 22:14

# Create your views here.
def index(request):
    tasks = Tasks.objects.all() 
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context  = {'tasks':tasks, 'form':form}
    return render(request,'tasks/lists.html', context)


def update_task(request,pk):
    item = Tasks.objects.get(id=pk)
    form = TaskForm(instance=item)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=item)
        if form.is_valid():
            form.save();
            return redirect('/')

    context = {'form':form}

    return render(request,'tasks/update_task.html', context)


def delete_task(request,pk):
    item = Tasks.objects.get(id=pk) 
    if request.method == "POST":
        item.delete()
        return redirect("/")
    context = {'item':item}
    return render(request,'tasks/delete.html',context)