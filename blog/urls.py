from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('blog_detail/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('create_article/', views.create_article, name='create_article'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('author/<slug:slug>/', views.author, name='author'),
    path('specific_category/', views.specific_category, name='specific_category'),
]

urlpatterns += staticfiles_urlpatterns()