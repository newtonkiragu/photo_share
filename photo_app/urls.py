from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/edit/', views.account_edit, name='account_edit'),
    path('accounts/profile/', views.account_profile, name='account_profile'),
    path('<username>/', views.user_profile, name='user_profile'),
]