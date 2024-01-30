from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    used = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['name', 'used']
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cook_book:product_detail', args=[self.id, self.slug])


class Recipe(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cook_book:recipe_detail', args=[self.id, self.slug])


class RecipeItem(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='recipe_items', on_delete=models.CASCADE)
    weight = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.pk}'

