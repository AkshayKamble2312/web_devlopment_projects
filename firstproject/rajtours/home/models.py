from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Contact(models.Model):
    firstname=models.CharField(max_length=150)
    lastname=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    phone=models.CharField(max_length=12)
    city=models.CharField(max_length=150)
    state=models.CharField(max_length=150)
    zip=models.CharField(max_length=150)
    

def __str__(self):
    return self.name

