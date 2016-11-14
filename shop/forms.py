#coding:utf-8
from django import forms
from .models import *



class CategoryForm(forms.ModelForm):
	
    class Meta:
        model = Category	
        exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
class ProductForm(forms.ModelForm):
    	
    class Meta:
        model = Product
        exclude = [] # uncomment this line and specify any field to exclude it from the form

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
