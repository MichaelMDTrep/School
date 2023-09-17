from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.users, name='users'),
    path('<str:username>/', views.user, name='user')
]