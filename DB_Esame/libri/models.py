from django.db import models
from django.conf import settings

class Libro(models.Model):
    titolo = models.CharField(max_length=255)
    autore = models.CharField(max_length=255)
    descrizione = models.TextField(blank=True)
    genere = models.CharField(max_length=100)
    proprietario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.titolo
