from .models import Article, Comment
from django import forms

class CreateArticleForm(forms.ModelForm):
    intro = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 4}))
    class Meta:
        model = Article
        exclude = ['author', 'slug', 'author_profile']
        fields = '__all__'

class CommentForm(forms.ModelForm):
    body = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Add to the discussion'}))
    class Meta:
        model = Comment
        fields = ['body']      
    