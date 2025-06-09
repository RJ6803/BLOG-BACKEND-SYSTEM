from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('sign_up/', views.sign_up, name='users-sign-up'),
    path('profile/', views.profile, name='users-profile'),
    path('', auth_view.LoginView.as_view(template_name='users/login.html'), name='users-login'),
    path('logout/', views.custom_logout_view, name='users-logout'),

    # ✅ Password Reset Flow (corrected)
    path('password_reset/', auth_view.PasswordResetView.as_view(template_name='users/password_reset.html'), name='users-password-reset'),
    path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_view.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete'),
]

