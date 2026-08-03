from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    List_display = ['name', 'inventory', 'new_price']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['created', 'updated']