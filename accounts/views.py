from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import SignUpForm


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
            messages.success(request, 'Sign up successfully')
            form.save()
            return redirect('accounts:sign-in')

    context = {'form': form}
    return render(request, 'accounts/sign-up.html', context)

def sign_out(request):
    logout(request)
    return redirect('accounts:sign-in')