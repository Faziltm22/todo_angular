from django.db import models


# Create your models here.

class User(models.Model):
    Username=models.CharField(unique=True,max_length=100)
    Password=models.CharField(max_length=50)

class Todo(models.Model):
    Userid=models.ForeignKey(User,on_delete=models.CASCADE)
    Tododata=models.CharField(max_length=100) 


