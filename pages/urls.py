from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    # homepage
    path('', views.HomePageDetail, name='home'),
    # noticia
    path('noticia_detail/<int:pk>/', views.noticia_detail_view, name='noticia_detail'),
    path('noticias_list/', views.noticias_list_view, name='noticias_list'),
]
