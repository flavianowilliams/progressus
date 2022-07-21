from django.urls import path
from . import views

app_name = 'cadastros'

urlpatterns = [
    # perfis
    path('profiles_list/',views.perfis_list_view, name='profiles_list'),
    path('profile_delete/<int:pk>/', views.perfis_delete_view, name='profile_delete'),
    # chamadas
    path('chamadas_list/',views.chamadas_list_view, name='chamadas_list'),
    path('chamada_create/', views.chamadas_create_view, name='chamada_create'),
    path('chamada_delete/<int:pk>/', views.chamada_delete_view, name='chamada_delete'),
    path('chamada_update/<int:pk>/', views.chamada_update_view, name='chamada_update'),
]