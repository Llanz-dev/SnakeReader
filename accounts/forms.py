from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from django import forms

class ProfileForm(forms.ModelForm):
    profile_picture = forms.ImageField(required=False, error_messages = {'invalid': ("Image files only")}, widget=forms.FileInput)
    phone = forms.CharField(max_length=11, min_length=11, required=False)
    job_description = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 30}))
    class Meta:
        model = Profile
        exclude = ['user', 'user_slug']
        fields = '__all__'


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label='Username')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
        
class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text='Required. Inform a valid email address.')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'first_name', 'last_name', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
