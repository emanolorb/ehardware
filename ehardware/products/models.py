from django.db import models


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    sku = models.CharField(max_length=64, unique=True)
    presio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        ordering = ["id"]

    def __str__(self) -> str:
        return f"{self.nombre} ({self.sku})"
