from django.db import models

# Create your models here.

class Library(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    library = models.ForeignKey('Library', on_delete=models.CASCADE)

    def __str__(self):
        return self.name