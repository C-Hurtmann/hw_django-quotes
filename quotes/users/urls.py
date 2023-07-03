from django.contrib.auth.views import PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('signup/', views.signupuser, name='signup'),
    path('login/', views.loginuser, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('reset-password/', views.ResetPasswordView.as_view(), name='reset-password'), # first step
    path('reset-password/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'), # second step. Request for password reset has been sent
    path('reset-password/confirm/<uidb64>/<token>',
         PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',
                                          success_url='/users/reset-password/complete/'),
         name='password_reset_confirm'),
    path('reset-password/complete/',
         PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]