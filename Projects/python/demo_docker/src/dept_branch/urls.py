from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from dept_branch.views import DeptBranchListCreateAPIView, DeptBranchRetrieveUpdateDestroyAPIView


urlpatterns = [
	path('', DeptBranchListCreateAPIView.as_view()),
	path('<int:pk>', DeptBranchRetrieveUpdateDestroyAPIView.as_view()),

]
