from django.shortcuts import render
from django.views.generic import CreateView,FormView

# Create your views here.
from Main.forms import  CategoryForm
from Main.models import Task, Category


class CreateCategory(FormView):
    template_name = 'Main/test.html'
    success_url = '/success/'
    form_class = CategoryForm

    def form_valid(self,form):
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

def success(request):
    return render(request, 'Main/Success.html')


def all_tasks_by_user(request):
    tasks = Task.objects.all()
    categories = Category.objects.all()
    return render(request, 'Main/allTask.html', {'tasks': tasks, 'categories': categories})

def delete_task_by_id(request, id):
    task = Task.objects.get()
    return render(request, 'Main/allTask.html', {'tasks': tasks, 'categories': categories})

class CreateTask(CreateView):
    template_name = 'Main/addTask.html'
    model = Task
    fields = ['Title', 'Content', 'Status', 'Category','CreateDate','Owner']
    success_url = "http://localhost:8000/allTask/"


