from .models import Article
from django import forms

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['author', 'slug']
        fields = '__all__'
        