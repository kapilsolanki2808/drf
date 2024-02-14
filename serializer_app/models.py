from django.db import models

# Create your models here.
# class Comment:
# from datetime import datetime
# from django.utils import timezone

class Comment(models.Model):
    email = models.EmailField()
    content = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
 