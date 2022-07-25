import sys
from django.shortcuts import redirect, render
from .forms import CreateArticleForm
from accounts.forms import ProfileForm, UserUpdateForm
from .models import Article
from accounts.models import Profile
# Create your views here.

def home(request): 
    # article_objects = Article.objects.all().order_by('-id')[0:5]   
    # length_article = len(article_objects)
    # max_length = 5
    # blank_posts = max_length - length_article   
    # for data in range(0, length_article):  
    #     print('data:', article_objects[data])
    # for blank in range(blank_posts):
    #     print('blank:', blank)
    # print('Article objects:', article_objects)
    # print('Length article:', length_article)
        
    try:
        first_query = Article.objects.all().order_by('-id')[0]
    except:
        first_query = None
        
    second_third = Article.objects.all().order_by('-id')[1:3]  
    two_article = len(second_third)
    max_two = 2
    blank_posts = max_two - two_article   
    for data in range(0, two_article):  
        print('data:', second_third[data])
    for blank in range(blank_posts):
        print('blank:', blank)
    print('Article objects:', second_third)
    print('Length article:', two_article)
      
    two_list = len(second_third)
    if two_list < 1:
        two_list = 0
    elif two_list == 1:
        second_third = Article.objects.all().order_by('-id')[1:2]                            
        two_list = 1                     
    else:
        second_third = Article.objects.all().order_by('-id')[1:3]                                    
        two_list = 2      

    third_fourth = Article.objects.all().order_by('-id')[3:5]    
    three_list = len(third_fourth)

    if three_list < 1:
        three_list = 0
    elif three_list == 1:
        third_fourth = Article.objects.all().order_by('-id')[3:4]                            
        three_list = 1           
    else:
        third_fourth = Article.objects.all().order_by('-id')[3:5]                                    
        three_list = 2 
    
    context = {
                    'first_query': first_query,
                    'two_list': two_list,             
                    'second_third': second_third,
                    'third_fourth': third_fourth,               
                    'three_list': three_list
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
