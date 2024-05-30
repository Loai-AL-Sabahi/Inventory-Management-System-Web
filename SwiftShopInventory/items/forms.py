from django import forms
from .models import Item
INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image', 'stock')
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'stock': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'stock')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'stock': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }