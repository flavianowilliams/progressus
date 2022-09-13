from django.urls import path
from . import views

app_name = 'chamadas'

urlpatterns = [
    path('chamadas_abertas/', views.abertas_list_view,name='chamadas_abertas'),
    path('chamadas_andamento/', views.andamento_list_view, name='chamadas_andamento'),
    path('chamadas_encerradas/', views.encerradas_list_view, name='chamadas_encerradas'),
]