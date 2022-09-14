from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    # homepage
    path('', views.HomePageDetail, name='home'),
    # noticia
    path('noticia_detail/<int:pk>/', views.noticia_detail_view, name='noticia_detail'),
]

