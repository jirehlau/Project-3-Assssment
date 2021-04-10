from django.db import models

class Widget(models.Model):
    description = models.CharField(max_length=50)
    quantity = models.IntegerField()