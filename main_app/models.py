from django.db import models

class SW(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=100, default='1.0')
    description = models.TextField(default=None)
    model = models.CharField(max_length=100)  

    def __str__(self):
        return self.name

