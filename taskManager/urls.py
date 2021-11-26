"""taskManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', login_view),
    path('label/showAllLabels', showAllLabels),
    path('label/add', CreateLabel.as_view()),
    path('label/delete/<int:id>', deleteLabel),
    path('allTask/<pk>', all_tasks_by_user),
    path('task/add', CreateTask.as_view()),
    path('task/delete/<int:id>', deleteTask),
    path('category/add', CreateCategory.as_view()),
    path('category/delete/<int:id>', deleteCategory),
    path('user/add', CreateUser.as_view())




]
