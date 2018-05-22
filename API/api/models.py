from django.db import models

# Create your models here.
from rest_framework.compat import MinValueValidator, MaxValueValidator


class Feature(models.Model):
    feature_name = models.CharField(max_length=500, blank=True)


class Name(models.Model):
    fk = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='feature')
    name = models.CharField(max_length=500, blank=True)
    checked = models.IntegerField(default=0)
    total_time = models.FloatField(validators=[MinValueValidator(0.5), MaxValueValidator(100)])
    ios_developer = models.FloatField(validators=[MinValueValidator(0.5), MaxValueValidator(100)])
    android_developer = models.FloatField(validators=[MinValueValidator(0.5), MaxValueValidator(100)])
    backend_developer = models.FloatField(validators=[MinValueValidator(0.5), MaxValueValidator(100)])


class Template(models.Model):
    fk_template = models.ForeignKey(Name, on_delete=models.CASCADE, related_name='template')
    template_name = models.CharField(max_length=500, blank=True)
    url = models.URLField()
    check = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(1)], default=0)




