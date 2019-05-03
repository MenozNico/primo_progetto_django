from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    giornalist = models.ForeignKey('Giornalist', on_delete=models.CASCADE, related_name="articles")

    def __str__ (self):
        return self.title

class Giornalist(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)

    def __str__ (self):
        return self.name + " " + self.surname
