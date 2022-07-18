from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('profile/', views.profile_update_view, name='profile'),
    path('reset_password/', views.PasswordReset.as_view(), name="reset_password"),
    path('reset_password_sent/', views.PasswordResetDone.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(),name="password_reset_confirm"),
    path('reset_password_complete/', views.PasswordResetComplete.as_view(), name="password_reset_complete"),
]