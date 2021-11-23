from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField()
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
    UsersTags = models.ManyToManyField(User, related_name='users_tags')
    Owner = models.ForeignKey(User, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)







