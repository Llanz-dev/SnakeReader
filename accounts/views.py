from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import SignUpForm, ProfileForm
from accounts.models import Profile

# Create your views here.
def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user_account = form.get_user()
            login(request, user_account)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('blog:home')
        
    context = {'form': form}
    return render(request, 'accounts/sign-in.html', context)

def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_account = form.save()
            Profile.objects.create(user=user_account)
            messages.success(request, 'Sign up successfully')
            return redirect('accounts:sign-in')

    context = {'form': form}
    return render(request, 'accounts/sign-up.html', context)

def sign_out(request):
    logout(request)
    return redirect('accounts:sign-in')

def profile(request):
    form = ProfileForm(instance=request.user.profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            username = form.cleaned_data.get('first_name')
            if username == None:
                messages.success(request, f'Your account has been updated!')                
            else:
                messages.success(request, f'{username}, your account has been updated!')                
            form.save()
            return redirect('accounts:profile')
        
    context = {'form':form}
    return render(request, 'accounts/profile.html', context)
