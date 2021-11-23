from django.shortcuts import render

# Create your views here.
from Main.models import Task, Category


def all_tasks_by_user(request):
    tasks = Task.objects.all()
    categories = Category.objects.all()
    return render(request, 'Main/allTask.html', {'tasks': tasks, 'categories': categories})

