from django.shortcuts import redirect, render
from .forms import CreateArticleForm
from .models import Article
from accounts.models import Profile
# Create your views here.

def home(request): 
    article_objects = Article.objects.all()   
    
    context = {'article_objects': article_objects}
    return render(request, 'blog/home.html', context)


def create_article(request):
    article_form = CreateArticleForm()
    if request.method == 'POST':
        article_form = CreateArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            instance = article_form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog:home')
        
    context = {'article_form': article_form}
    return render(request, 'blog/create_article.html', context)


def blog_detail(request, slug):
    specific_article = Article.objects.get(slug=slug)
    
    context = {'specific_article': specific_article}
    return render(request, 'blog/blog_detail.html', context)


def about(request):
    context = {}
    return render(request, 'blog/about.html', context)


def contact(request):
    context = {}
    return render(request, 'blog/contact.html', context)


def author(request):
    context = {}
    return render(request, 'blog/author.html', context)


def specific_category(request):
    context = {}
    return render(request, 'blog/specific_category.html', context)
