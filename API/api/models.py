from django.db import models

# Create your models here.
class Feature(models.Model):
    feature_name = models.CharField(max_length=500, blank=True)

class Name(models.Model):
    fk = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='feature')
    name = models.CharField(max_length=500, blank=True)
    checked = models.BooleanField(default=False)
    time = models.CharField(max_length=200, blank=True)
    platform = models.CharField(max_length=200, blank=True)
