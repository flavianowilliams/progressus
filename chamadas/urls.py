from django.urls import path
from . import views

app_name = 'chamadas'

urlpatterns = [
    # chamada
    path('chamadas_abertas/', views.abertas_list_view,name='chamadas_abertas'),
    path('chamadas_andamento/', views.andamento_list_view, name='chamadas_andamento'),
    path('chamadas_encerradas/', views.encerradas_list_view, name='chamadas_encerradas'),
    path('chamadas_list_superuser/', views.chamada_list_superuser_view, name='chamadas_list_superuser'),
    path('inscricao_list_user/', views.inscricao_list_user, name='inscricao_list_user'),
    # inscricao
    path('chamada_inscricao/<int:pk>/', views.inscricao_create_view, name='chamada_inscricao'),
    path('inscricoes_list_superuser/<int:pk>/', views.inscricao_list_superuser, name='inscricoes_list_superuser'),
    path('inscricao_delete/<int:pk>/', views.inscricao_delete_superuser, name='inscricao_delete'),
    path('inscricao_update/<int:pk>/', views.inscricao_update_view, name='inscricao_update'),
    path('inscricao_sendmail/<int:pk>/', views.enviar_email, name='inscricao_sendmail'),
    path('inscricao_detail/<int:pk>/', views.inscricao_detail_view, name='inscricao_detail'),
    # projeto
    path('projetos_list/<int:pk>/', views.projeto_list_view, name='projetos_list'),
    path('projeto_detail_superuser/<int:pk>/', views.projeto_detail_list_view, name='projeto_detail_superuser'),
    path('introducao_detail_superuser/<int:pk>/', views.introducao_detail_superuser, name='introducao_detail_superuser'),
]