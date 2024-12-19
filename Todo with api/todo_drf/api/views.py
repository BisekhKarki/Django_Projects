from django.shortcuts import render
from .models import Task
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer


# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_url ={
        'List':'/task-list/',
        'Detail view':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',
    }

    return Response(api_url)

#Get all the tasks 
@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('id')
    serializer = TaskSerializer(tasks,many=True)
    return Response(serializer.data)

# Get each task details
@api_view(['GET'])
def taskDetail(request,pk):
    tasks = Task.objects.get(id=pk)
    seralizer = TaskSerializer(tasks,many=False)
    return Response(seralizer.data)


# Create Tasks
@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# Update Tasks based on id
@api_view(['POST'])
def taskUpdate(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance =tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


# To delete a task
@api_view(['DELETE'])
def taskDelete(request,pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response("Task Deleted")

