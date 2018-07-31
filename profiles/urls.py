from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('/accounts/edit', views.edit_account, name='edit_account'),
]