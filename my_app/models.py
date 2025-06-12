from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=20,null=True,blank=True,unique=True)
    # def __str__(self):
    #     return self.category_name