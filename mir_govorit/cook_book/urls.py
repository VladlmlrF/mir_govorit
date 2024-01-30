from django.urls import path
from .views import *

app_name = 'cook_book'

urlpatterns = [
    path('', home, name='home'),
    path('products', product_list, name='product_list'),
    path('products/<int:id>/<slug:slug>/', product_detail, name='product_detail'),
    path('recipes', recipe_list, name='recipe_list'),
    path('recipes/<int:id>/<slug:slug>/', recipe_detail, name='recipe_detail'),
    path('recipes/update/<int:recipe_id>/', add_product_to_recipe, name='recipe_update'),
    path('recipes/cook/<int:recipe_id>/', cook_recipe, name='cook_recipe'),
    path('recipes/without-product/<int:product_id>', show_recipes_without_product, name='without_product'),
]
