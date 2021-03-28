from django.contrib import admin

from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):

    list_display = ['name', 'price', 'stock', 'slug', 'created_at', 'updated_at', 'active']
    