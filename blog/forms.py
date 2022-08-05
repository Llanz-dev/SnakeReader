from .models import Article
from django import forms

class CreateArticleForm(forms.ModelForm):
    intro = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 4}))
    class Meta:
        model = Article
        exclude = ['author', 'slug', 'author_profile']
        fields = '__all__'
        