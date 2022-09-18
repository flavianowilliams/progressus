from django.urls import path
from . import views

app_name = 'chamadas'

urlpatterns = [
    # chamada
    path('chamadas_abertas/', views.abertas_list_view,name='chamadas_abertas'),
    path('chamadas_andamento/', views.andamento_list_view, name='chamadas_andamento'),
    path('chamadas_encerradas/', views.encerradas_list_view, name='chamadas_encerradas'),
    path('chamadas_list_superuser/', views.chamada_list_superuser_view, name='chamadas_list_superuser'),
    path('chamadas_list_user/', views.chamada_list_user, name='chamadas_list_user'),
    # inscricao
    path('chamada_inscricao/<int:pk>/', views.inscricao_create_view, name='chamada_inscricao'),
    path('inscricoes_list_superuser/<int:pk>/', views.inscricao_list_superuser, name='inscricoes_list_superuser'),
    path('inscricao_delete/<int:pk>/', views.inscricao_delete_superuser, name='inscricao_delete'),
    path('inscricao_update/<int:pk>/', views.inscricao_update_view, name='inscricao_update'),
    path('inscricao_sendmail/<int:pk>/', views.enviar_email, name='inscricao_sendmail'),
    path('inscricao_detail/<int:pk>/', views.inscricao_detail_view, name='inscricao_detail'),
]