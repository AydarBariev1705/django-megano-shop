from django.contrib import admin
from .models import (Product,
                     Tag,
                     Review,
                     Category,
                     Sale,
                     ProductSpecification,
                     ProductImage,
                     CategoryImage)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'pk', 'title'
    list_display_links = 'pk', 'title'
    ordering = 'pk',


@admin.register(CategoryImage)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'pk', 'src'
    list_display_links = 'pk', 'src'
    ordering = 'pk',


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = 'pk', 'title', 'price', 'category', 'archived'
    list_display_links = 'pk', 'title'
    ordering = 'pk',


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name',
    list_display_links = 'pk', 'name'
    ordering = 'pk',


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = 'pk', 'author', 'product', 'date'
    list_display_links = 'pk',
    ordering = 'pk',


@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = 'pk', 'product',
    list_display_links = 'pk',
    ordering = 'pk',


@admin.register(ProductSpecification)
class ProductSpecificationAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name', 'value', 'product'
    list_display_links = 'pk', 'name'
    ordering = 'pk',


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name', 'product'
    list_display_links = 'pk', 'name'
    ordering = 'pk',
