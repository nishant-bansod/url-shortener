from django import forms
from .models import ShortURL

class URLForm(forms.ModelForm):
    class Meta:
        model = ShortURL
        fields = ['original_url']
        labels = {'original_url': 'Enter Your Long URL'}
        widgets = {
            'original_url': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com/your-long-url'
            })
        }
