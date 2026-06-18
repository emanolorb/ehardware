from django.db import models


class Address(models.Model):
    pk = models.CompositePrimaryKey("codigo_postal", "asentamiento")
    codigo_postal = models.CharField(max_length=5)
    estado = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    tipo_asentamiento = models.CharField(max_length=255)
    asentamiento = models.CharField(max_length=255)
    clave_oficina = models.CharField(max_length=64, unique=True)

    class Meta:
        ordering = ["codigo_postal"]

    def __str__(self) -> str:
        return f"{self.estado} ({self.sku})"
    
