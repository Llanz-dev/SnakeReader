from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('sign-out/', views.sign_out, name='sign-out'),
    path('profile/', views.profile, name='profile'),
    path('confirmation-delete/', views.confirmation_delete, name='confirmation_delete'),
]
