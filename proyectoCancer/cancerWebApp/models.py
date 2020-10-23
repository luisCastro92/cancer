from django.db import models

# Create your models here.
class TejidoMama(models.Model):
    
    parteP = models.IntegerField()
    temp = models.FloatField()
    color = models.FloatField()
    inflamacion = models.FloatField()