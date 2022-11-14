from django.db import models

# Create your models here.


class Books(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
 
    isbn=models.CharField(max_length=17)
    author=models.CharField(max_length=200)


