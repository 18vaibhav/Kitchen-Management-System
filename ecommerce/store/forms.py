from django import forms

# class ProductForm(forms.Form):
# 	name = forms.CharField()
#     price = forms.IntegerField()
#     image = forms.ImageField()


class ProductForm(forms.Form):
    name = forms.CharField()
    price = forms.FloatField()
    image = forms.ImageField()