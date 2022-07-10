from .forms import SignUpForm, ProfileForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib import messages
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

@login_required
def profile(request):
    profile_form = ProfileForm(instance=request.user.profile)
    user_form = UserUpdateForm(instance=request.user)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        user_form = UserUpdateForm(request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            username = user_form.cleaned_data.get('username')
            if username == None:
                messages.success(request, f'Your account has been updated!')                
            else:
                messages.success(request, f'{username}, your account has been updated!')                
            profile_form.save()
            user_form.save()
            return redirect('accounts:profile')
        
    context = {'profile_form': profile_form, 'user_form': user_form}
    return render(request, 'accounts/profile.html', context)
