from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Account(models.Model):
  account_name = models.CharField(max_length=100) 
  users = models.ForeignKey(User, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.account_name

# class Hello(models.Model):
#   name = models.CharField(max_length=111)