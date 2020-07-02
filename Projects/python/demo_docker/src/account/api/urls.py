from django.urls import path
from account.api.views import(
	registration_view,
)

from rest_framework.authtoken.views import obtain_auth_token
from account.views import UserListCreateAPIView, AccountRetrieveUpdateAPIView,AccountListAPIView

app_name = 'account'

urlpatterns = [
	path('register', registration_view, name="register"),
	path('login', obtain_auth_token, name="login"),
	path('', UserListCreateAPIView.as_view(), name='user-list-create-api')
	path('<int:pk>', AccountListAPIView.as_view(), name='user-list-create-api')

]
