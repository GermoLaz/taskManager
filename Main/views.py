from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def login_view(request):
    if request.method == 'GET':
        return render(request,'Main/form.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return all_tasks_by_user(request)
        else:
            return render(request,'Main/form.html')

from Main.models import Task, Category
from django.contrib.auth.decorators import login_required

@login_required
def all_tasks_by_user(request):
    tasks = Task.objects.all()
    categories = Category.objects.all()
    return render(request, 'Main/allTask.html', {'tasks': tasks, 'categories': categories})

