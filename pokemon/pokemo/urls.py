from django.urls import path
from . import views

urlpatterns = [
    path('', views.pokemon_list, name='pokemon_list'),  
    path('pokemon/<int:pk>/', views.pokemon_detail, name='pokemon_detail'),  
    path('pokemon/new/', views.pokemon_create, name='pokemon_create'),  
    path('pokemon/edit/<int:pk>/', views.pokemon_edit, name='pokemon_edit'),  
    path('pokemon/delete/<int:pk>/', views.pokemon_confirm_delete, name='pokemon_confirm_delete'),  
]
