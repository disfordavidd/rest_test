from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50)
    new = models.BooleanField(default=False)
    added = models.DateTimeField()
    
    class Meta:
        ordering = ['added']
    