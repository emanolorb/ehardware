from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "sku", "presio"]
    search_fields = ["nombre", "sku"]
    ordering = ["id"]
