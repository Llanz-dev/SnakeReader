from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('author/', views.author, name='author'),
    path('specific_category/', views.specific_category, name='specific_category'),
]
