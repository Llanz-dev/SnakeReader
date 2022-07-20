from djrichtextfield.widgets import RichTextWidget
from .models import Article
from django import forms
class CreateArticleForm(forms.ModelForm):
    intro = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 4, 'cols': 200}))

    class Meta:
        model = Article
        exclude = ['author', 'slug']
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super(CreateArticleForm, self).__init__(*args, **kwargs)
    #     self.fields['intro'].label = "New Email Label"