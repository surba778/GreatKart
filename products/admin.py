from django.contrib import admin
from .models import Product, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    # fields to display within admin dash
    list_display = (
        'name',
        'category',
        'price',
        'rating',
        'image',
    )


class CategoryAdmin(admin.ModelAdmin):
    # fields to display within admin dash
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
