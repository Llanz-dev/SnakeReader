from django.contrib import messages
from .forms import SignUpForm
from django.shortcuts import redirect, render

# Create your views here.


def sign_in(request):
    context = {}
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
