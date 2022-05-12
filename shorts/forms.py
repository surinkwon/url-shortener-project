from django import forms
from .models import ShortUrl

class ShortUrlForm(forms.ModelForm):
    original_url = forms.URLField(widget=forms.URLInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a URL you want to shorten'
        }
    ))

    class Meta:
        model = ShortUrl
        fields = ('original_url',)


class CustomShortUrlForm(forms.ModelForm):
    original_url = forms.URLField(widget=forms.URLInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Write a URL you want to shorten'
        }
    ))

    url_name = forms.CharField(widget=forms.TextInput(
        attrs={
        'class': 'form-control',
        'placeholder': 'Write a name you want to custom',
        'style': 'width: 20rem'
    }))

    class Meta:
        model = ShortUrl
        fields = '__all__'