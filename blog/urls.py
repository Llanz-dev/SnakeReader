from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('blog-detail/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('create-article/', views.create_article, name='create_article'),
    path('update-article/<slug:slug>/', views.update_article, name='update_article'),
    path('delete-article/<slug:slug>/', views.delete_article, name='delete_article'),
    path('about/', views.about, name='about'),
    path('add-comment/<slug:slug>/', views.add_comment, name='add_comment'),
    path('delete-comment/<int:pk>/<slug:slug>/', views.delete_comment, name='delete_comment'),
    path('edit-comment/<int:pk>/<slug:slug>/', views.edit_comment, name='edit_comment'),
    path('contact/', views.contact, name='contact'),
    path('author/<slug:user_slug>/', views.author, name='author'),
    path('category/<slug:slug>/', views.specific_category, name='specific_category'),    
    path('title-duplicate-error/<str:title_entered>/', views.title_duplicate_error, name='title_duplicate_error'),    
]

urlpatterns += staticfiles_urlpatterns()