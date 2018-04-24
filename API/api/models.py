from django.db import models

# Create your models here.

class Vprasanja(models.Model):
    vprasanje = models.CharField(max_length=500)

    def __str__(self):
        return self.vprasanje

class Odgovori(models.Model):
    vprasanje = models.ForeignKey(Vprasanja, on_delete=models.CASCADE, related_name='odg')
    odgovor1 = models.CharField(max_length=200, blank=True)
    odgovor2 = models.CharField(max_length=200, blank=True)
    odgovor3 = models.CharField(max_length=200, blank=True)
    odgovor4 = models.CharField(max_length=200, blank=True)
    odgovor5 = models.CharField(max_length=200, blank=True)
    odgovor6 = models.CharField(max_length=200, blank=True)
    odgovor7 = models.CharField(max_length=200, blank=True)
    odgovor8 = models.CharField(max_length=200, blank=True)
    odgovor9 = models.CharField(max_length=200, blank=True)
    odgovor10 = models.CharField(max_length=200, blank=True)
    platforma = models.CharField(max_length=200)
