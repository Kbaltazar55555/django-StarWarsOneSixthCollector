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
    description = models.TextField(max_length=100)
    tools_Used = models.TextField(max_length=100)
    sw = models.ForeignKey(SW, on_delete=models.CASCADE, null=True)  # Moved inside the class

    def __str__(self):
        return self.name





