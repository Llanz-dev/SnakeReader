import sys
from django.shortcuts import redirect, render
from .forms import CreateArticleForm
from accounts.forms import ProfileForm, UserUpdateForm
from .models import Article
from accounts.models import Profile
# Create your views here.

def home(request): 
    article_objects_left = Article.objects.all().order_by('-id')[0:5]   
    article_objects_right = Article.objects.all().order_by('-id')[5:11]   
    length_article_left = len(article_objects_left)
    length_article_right = len(article_objects_right)
    max_length = 5
    blank_posts_left = max_length - length_article_left   
    blank_posts_right = max_length - length_article_right   
     
    
    context = {
                    'article_objects_left': article_objects_left,
                    'article_objects_right': article_objects_right,
                    'blank_posts_left': range(blank_posts_left),
                    'blank_posts_right': range(blank_posts_right),
                }
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


def author(request, slug):
    first_query = Article.objects.get(slug=slug)
    
    context = {'first_query': first_query}
    return render(request, 'blog/author.html', context)


def specific_category(request):
    context = {}
    return render(request, 'blog/specific_category.html', context)
