from django.db import models

# Create your models here.

class Emp(models.Model):
    uname = models.CharField(max_length=30)
    email= models.EmailField()
    password=models.CharField(max_length=10)

class Blog(models.Model):
    image = models.ImageField(upload_to='image/')
    title = models.CharField(max_length=30)
    desc = models.TextField(max_length=200)
    postby= models.CharField(max_length=20)
