from django.urls import path

from account.views import UserListCreateAPIView, UserLogin, PasswordSet, ChangePassword, AccountListAPIView


urlpatterns = [
   
    path('', UserListCreateAPIView.as_view(), name='user-list-create-api'),
	path('show', AccountListAPIView.as_view()),
    path('login', UserLogin.as_view(), name='user-login-`api'),
    path('passwordset', PasswordSet.as_view(),),
    path('passwordreset', ChangePassword.as_view(), name='password-reset-`api'),

    
]
