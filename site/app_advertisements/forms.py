from typing import Any, Dict, Mapping, Optional, Type, Union
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Advertisement
from django.core.exceptions import ValidationError
from django import forms


# class AdvertisementForm(forms.ModelForm):
#     class Meta:
#         model = Advertisement
#         fields = ['title','description','price','auction','image']
#         widgets = {'title' : forms.TextInput(attrs={'class': 'form-control form-control-lg'}), 
#                    'description' : forms.Textarea(attrs={'class': 'form-control form-control-lg'}), 
#                    'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}), 
#                    'auction' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
#                    'image': forms.FileInput(attrs={'class': 'form-control form-control-lg'})}
        

class AdvertisementForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['description'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['image'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['price'].widget.attrs['class'] = 'form-control form-control-lg'
        self.fields['auction'].widget.attrs['class'] = 'form-check-input'

    class Meta:
        model = Advertisement
        fields = ['title','description','price','auction','image']
        
    def clean_title(self):
        title = self.cleaned_data['title']
        if title.startswith('?'):
            raise ValidationError('Заголовок не может начинаться с вопросительного знака.')
        return title