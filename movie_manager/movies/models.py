from django.db import models

class movies(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField(null=True)
    description = models.CharField(max_length=120)# Ensure the field is defined correctly
