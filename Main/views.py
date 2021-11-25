from datetime import date

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView,FormView,DeleteView

from Main.models import Task, Category, Label
from django.contrib.auth.decorators import login_required

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




#TASK---------
@login_required
def all_tasks_by_user(request):
    tasks = Task.objects.all()
    categories = Category.objects.all()
    return render(request, 'Main/allTask.html', {'tasks': tasks, 'categories': categories})


class DeleteTask(DeleteView):
    model = Task
    success_url = '/allTask'


class CreateTask(CreateView):
    model = Task
    fields = ['Title','Content','Status']
    template_name = 'Main/label.html'
    success_url = '/allTask'

    def get_initial(self):
        self.initial = {"category": 1, "Owner": 1, "CreateDate": date.today()}
        return self.initial.copy()






#LABEL
def showAllLabels(request):
    labels = Label.objects.all()
    return render(request, 'Main/AllLabels.html', {'labels': labels})


class DeleteLabel(DeleteView):
    model = Label
    success_url ='/allTask'


class CreateLabel(CreateView):
    model = Label
    fields = ['Title','Color']
    template_name = 'Main/label.html'
    success_url = '/allTask'






