from datetime import date

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView,FormView,DeleteView

from Main.models import Task, Category, Label, User
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
            return all_tasks_by_user(request, user.id)
        else:
            return render(request,'Main/form.html')


#TASK---------
@login_required
def all_tasks_by_user(request,pk):
    tasks = Task.objects.filter(Owner_id = pk)
    categories = Category.objects.all()
    return render(request, 'Main/allTask.html', {'tasks': tasks, 'categories': categories})


@login_required
def deleteTask(request,id):
    Task.objects.filter(id=id).delete()
    return redirect('/allTask/'+ str(request.user.id))

class CreateTask(CreateView):
    model = Task
    fields = ['Title','Content','Status','CreateDate','Category']
    template_name = 'Main/task.html'
    success_url = '/allTask'

    def post(self, request):
        form = self.get_form()

        if form.is_valid():
            Task.objects.create(Title = form.data['Title'],Content = form.data['Content'],Status_id = form.data['Status'],CreateDate = form.data['CreateDate'],Category_id = form.data['Category'], Owner_id = request.user.id)
            return redirect('/allTask/'+ str(request.user.id))

    # def get_initial(self):
    #     categoryThis = Category.objects.get(id = self.kwargs.get('Category_id'))
    #     userThis = MyUser.objects.get(id=self.request.user.id)
    #
    #     self.initial = {"Category_id": categoryThis.id , "Owner": userThis}
    #     return self.initial.copy()

@login_required
def showAllLabels(request):
    labels = Label.objects.all()
    return render(request, 'Main/AllLabels.html', {'labels': labels})

@login_required
def deleteLabel(request,id):
    Label.objects.filter(id=id).delete()
    return redirect('/label/showAllLabels')

class CreateLabel(CreateView):
    model = Label
    fields = ['Title','Color']
    template_name = 'Main/label.html'
    success_url = '/allTask'
    def post(self, request):
        form = self.get_form()

        if form.is_valid():
            Label.objects.create(Title=form.data['Title'], Color=form.data['Color'])
            return redirect('/allTask/'+ str(request.user.id))

@login_required
def deleteCategory(request,id):
    Category.objects.filter(id=id).delete()
    return redirect('/allTask/'+ str(request.user.id))

class CreateCategory(CreateView):
    model = Category
    fields = ['Title']
    template_name = 'Main/category.html'
    success_url = '/allTask'

    def post(self, request):
        form = self.get_form()

        if form.is_valid():
            Category.objects.create(Title=form.data['Title'])
            return redirect('/allTask/'+ str(request.user.id))

class CreateUser(CreateView):
    model = User
    fields = ['username', 'email', 'password']
    template_name = 'Main/signin.html'
    success_url = '/login'





