from django.db import models

# Create your models here.
class Instrument(models.Model):
    manufacturer = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    part_number = models.CharField(max_length=100, unique=True)
    range = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.manufacturer} - {self.model} ({self.part_number})"
