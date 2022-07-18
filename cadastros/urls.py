from django.urls import path
from . import views

app_name = 'cadastros'

urlpatterns = [
    path('profiles_list/',views.perfis_list_view, name='profiles_list'),
    path('profile_delete/<int:pk>/', views.perfis_delete_view, name='profile_delete'),
]