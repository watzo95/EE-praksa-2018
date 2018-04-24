from django.db import models

# Create your models here.

class Survey(models.Model):
    trajanje = models.CharField(max_length=200)
    stroski = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    ustvarjeno = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return '%s %s %s' % (self.trajanje, self.stroski, self.mail)

