from django.contrib import admin
from .models import Product, Recipe, RecipeItem


class RecipeItemInline(admin.TabularInline):
    model = RecipeItem
    raw_id_fields = ['product']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'used']
    list_filter = ['name', 'used']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [RecipeItemInline]
