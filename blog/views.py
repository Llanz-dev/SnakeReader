from django.shortcuts import render

# Create your views here.


def home(request):
    context = {}
    return render(request, 'blog/home.html', context)


def blog(request):
    context = {}
    return render(request, 'blog/blog.html', context)


def about(request):
    context = {}
    return render(request, 'blog/about.html', context)


def contact(request):
    context = {}
    return render(request, 'blog/contact.html', context)


def profile(request):
    context = {}
    return render(request, 'blog/profile.html', context)


def author(request):
    context = {}
    return render(request, 'blog/author.html', context)


def specific_category(request):
    context = {}
    return render(request, 'blog/specific_category.html', context)
