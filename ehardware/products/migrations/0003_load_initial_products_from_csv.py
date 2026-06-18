from __future__ import annotations

import csv
from decimal import Decimal
from pathlib import Path

from django.db import migrations


CSV_FILENAME = "catalogo_productos_hardware_demo.csv"


def load_initial_products(apps, schema_editor):
    Product = apps.get_model("products", "Product")
    base_dir = Path(__file__).resolve().parents[3]
    csv_path = base_dir / CSV_FILENAME

    if not csv_path.exists():
        # Keep migration safe for environments where seed data is optional.
        return

    with csv_path.open(encoding="utf-8-sig", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        products = []
        for row in reader:
            sku = (row.get("SKU") or "").strip()
            nombre = (row.get("Producto") or "").strip()
            precio_venta = (row.get("Precio_Venta_USD") or "").strip()

            if not sku or not nombre or not precio_venta:
                continue

            products.append(
                Product(
                    sku=sku,
                    nombre=nombre,
                    presio=Decimal(precio_venta),
                ),
            )

    if products:
        Product.objects.bulk_create(products, ignore_conflicts=True)


def unload_initial_products(apps, schema_editor):
    Product = apps.get_model("products", "Product")
    base_dir = Path(__file__).resolve().parents[3]
    csv_path = base_dir / CSV_FILENAME

    if not csv_path.exists():
        return

    skus = []
    with csv_path.open(encoding="utf-8-sig", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sku = (row.get("SKU") or "").strip()
            if sku:
                skus.append(sku)

    if skus:
        Product.objects.filter(sku__in=skus).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_rename_precio_product_presio"),
    ]

    operations = [
        migrations.RunPython(load_initial_products, unload_initial_products),
    ]
