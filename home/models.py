from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    admission_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    marks=models.IntegerField(null=True, blank=True)


class Blog(models.Model):
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=150)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    editor=models.ManyToManyField(User,related_name="edited_blogs", blank=True)
    created=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    