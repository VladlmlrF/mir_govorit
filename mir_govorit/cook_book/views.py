from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Product, Recipe, RecipeItem
from .forms import RecipeAddProductForm


def home(request):
    return render(request, 'cook_book/home.html')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'cook_book/product/list.html', {'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, 'cook_book/product/detail.html', {'product': product})


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'cook_book/recipe/list.html', {'recipes': recipes})


def recipe_detail(request, id, slug):
    recipe = get_object_or_404(Recipe, id=id, slug=slug)
    items = RecipeItem.objects.filter(recipe__id=id)
    return render(request, 'cook_book/recipe/detail.html', {'recipe': recipe, 'items': items})


def add_product_to_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    items = RecipeItem.objects.filter(recipe__id=recipe_id)
    if request.method == 'POST':
        form = RecipeAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            product = get_object_or_404(Product, id=cd['product_id'])
            for item in items:
                if item.product == product:
                    item.weight = cd['weight']
                    item.save()
                    return redirect('cook_book:recipe_detail', id=recipe_id, slug=recipe.slug)
            new_item = RecipeItem.objects.create(
                recipe=recipe,
                product=product,
                weight=cd['weight']
            )
            return redirect('cook_book:recipe_detail', id=recipe_id, slug=recipe.slug)
    else:
        form = RecipeAddProductForm()
    return render(
        request,
        'cook_book/recipe/update.html',
        {'form': form, 'recipe': recipe, 'items': items}
    )


def cook_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    items = RecipeItem.objects.filter(recipe__id=recipe_id)
    for item in items:
        product = item.product
        product.used += 1
        product.save()
    return redirect('cook_book:recipe_detail', id=recipe_id, slug=recipe.slug)


def show_recipes_without_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    recipe_items = RecipeItem.objects.filter(product=product, weight__gte=10)
    all_recipes = Recipe.objects.all()
    recipes_with_product = set()
    for item in recipe_items:
        recipe = item.recipe
        recipes_with_product.add(recipe)
    result = [a for a in all_recipes if a not in recipes_with_product]
    return render(request, 'cook_book/recipe/without_product.html', {'recipes': result})
