from django.db import models


class Laptop(models.Model):
    brand = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self) -> str:
        return f"{self.brand} {self.model_name}"
