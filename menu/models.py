from django.db import models


# Create your models here.


class Modules(models.Model):
    nom = models.CharField(max_length=200)
    fonction = models.CharField(max_length=400)
    prix = models.FloatField(default=0)
    eurorack = models.BooleanField(default=False)

    def __str__(self):
        return self.nom
