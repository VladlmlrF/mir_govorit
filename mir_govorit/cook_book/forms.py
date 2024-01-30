from django import forms


class RecipeAddProductForm(forms.Form):
    product_id = forms.IntegerField(min_value=1)
    weight = forms.IntegerField(min_value=1)
