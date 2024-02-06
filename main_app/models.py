from django.db import models

class SW(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=100, default='1.0')
    description = models.TextField(default=None)
    model = models.CharField(max_length=100)  

    def __str__(self):
        return self.name

# Adding new model for SW customs 
class Custom(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField(default='')
    tools_Used = models.TextField(default='')

sw = models.ForeignKey(SW, on_delete=models.CASCADE, related_name='customs')

def __str__(self):
    return self.name




