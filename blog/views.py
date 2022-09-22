from django.contrib.auth.decorators import login_required
from .forms import CreateArticleForm, CommentForm
from django.shortcuts import redirect, render
from .models import Article, Comment
from accounts.models import Profile
from django.contrib import messages
# Create your views here.

def home(request): 
    article_objects_left = Article.objects.all().order_by('-id')[0:5]   
    article_objects_right = Article.objects.all().order_by('-id')[5:10]   
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

@login_required
def create_article(request):
    article_form = CreateArticleForm()
    profile_account = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        article_form = CreateArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            
            # If the title entered was already in the article it will detect and avoid the integrity error.
            title_entered = article_form.cleaned_data.get('title')
            if Article.objects.filter(title=title_entered).exists():
                return redirect('blog:title_duplicate_error', title_entered)  
            # End
            
            instance = article_form.save(commit=False)
            instance.author = request.user
            instance.author_profile = profile_account
            instance.save()
            return redirect('blog:home')           
            
    context = {'article_form': article_form}
    return render(request, 'blog/create_article.html', context)         

def blog_detail(request, slug):
    specific_article = Article.objects.get(slug=slug)
    profile_author = Profile.objects.get(user=specific_article.author)                 
    
    context = {'specific_article': specific_article, 'profile_author': profile_author}    
    return render(request, 'blog/blog_detail.html', context)

@login_required
def update_article(request, slug):
    article = Article.objects.get(slug=slug)
    article_form = CreateArticleForm(instance=article)
    update_article = True
    if request.method == 'POST':
        article_form = CreateArticleForm(request.POST, request.FILES, instance=article)
        if article_form.is_valid():
            messages.warning(request, 'Article has been updated')
            article_form.save()
            return redirect('blog:blog_detail', article.slug)
    
    context = {'article_form': article_form, 'update_article': update_article}
    return render(request, 'blog/create_article.html', context)   

@login_required
def delete_article(request, slug):
    article = Article.objects.get(slug=slug)
    if request.method == 'POST':
        messages.error(request, 'Article has been deleted')                
        article.delete()
        return redirect('blog:home')
    
    context = {'article': article}
    return render(request, 'blog/delete_article.html', context)

def about(request):
    context = {}
    return render(request, 'blog/about.html', context)

def contact(request):
    context = {}
    return render(request, 'blog/contact.html', context)

def author(request, user_slug):
    author_info = Profile.objects.get(user_slug=user_slug)
    author_article = Article.objects.filter(author_profile=author_info)
    
    context = {'author_info': author_info, 'author_article': author_article}
    return render(request, 'blog/author.html', context)

def specific_category(request, slug):
    category = Article.objects.filter(category_choices=slug)
    no_category = False
    if not len(category):
        no_category = True
        
    context = {'category': category, 'slug': slug, 'no_category': no_category}
    return render(request, 'blog/specific_category.html', context)

@login_required
def add_comment(request, slug):
    specific_article = Article.objects.get(slug=slug)
    comment_form = CommentForm()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            instance = comment_form.save(commit=False)
            instance.author_profile = request.user.profile
            instance.article = specific_article
            instance.save()
            return redirect('blog:blog_detail', slug)   
        
    context = {'comment_form': comment_form}
    return render(request, 'blog/comment_add.html', context)
    

def delete_comment(request, pk, slug):
    Comment.objects.get(pk=pk).delete()
    return redirect('blog:blog_detail', slug)

def edit_comment(request, pk, slug):
    comment = Comment.objects.get(pk=pk)
    comment_form = CommentForm(instance=comment)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('blog:blog_detail', slug)
            
    context = {'comment_form': comment_form}
    return render(request, 'blog/comment_add.html', context)

def title_duplicate_error(request, title_entered):

    context = {'title_entered': title_entered}
    return render(request, 'blog/title_duplicate_error.html', context)
