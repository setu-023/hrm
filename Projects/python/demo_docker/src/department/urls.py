from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token
from department.views import DepartmentListCreateAPIView, DepartmentRetrieveUpdateDestroyAPIView

app_name = 'account'

urlpatterns = [
	path('', DepartmentListCreateAPIView.as_view()),
	path('<int:pk>', DepartmentRetrieveUpdateDestroyAPIView.as_view()),

]
