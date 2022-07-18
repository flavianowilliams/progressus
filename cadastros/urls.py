from django.urls import path
from . import views

app_name = 'cadastros'

urlpatterns = [
    path('profiles_list/',views.perfis_list_view, name='profiles_list'),
]