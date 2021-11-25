from django.contrib import admin
from Main.models import User, Label, Category, Task

# Register your models here.
admin.site.register(Label)
admin.site.register(Category)
admin.site.register(Task)

