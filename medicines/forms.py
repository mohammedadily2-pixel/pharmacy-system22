from django import forms
from .models import Medicine

class MedicineForm(forms.ModelForm):
    class Meta:
        model  = Medicine
        fields = [
            'name', 'category', 'quantity',
            'price', 'manufacture_date',
            'expiry_date', 'supplier', 'description'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Jina la dawa...'
            }),
            'category': forms.Select(attrs={'class': 'form-input'}),
            'quantity': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': '0'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': '0.00'
            }),
            'manufacture_date': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date'
            }),
            'expiry_date': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date'
            }),
            'supplier': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Jina la msambazaji...'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-input',
                'rows': 3,
                'placeholder': 'Maelezo ya ziada...'
            }),
        }