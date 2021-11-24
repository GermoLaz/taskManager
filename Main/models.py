from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MyUser(User):
    friends = models.ManyToManyField("self")


class Label(models.Model):
    Title = models.CharField(max_length=200)
    Color = models.CharField(max_length=200)


class Category(models.Model):
    Title = models.CharField(max_length=200)


class Task(models.Model):
    Title = models.CharField(max_length=200)
    Content = models.TextField(max_length=200)
    CreateDate = models.DateField(max_length=200)
    Status = models.ForeignKey(Label, on_delete=models.CASCADE)
    UsersTags = models.ManyToManyField(MyUser, related_name='users_tags')
    Owner = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)







