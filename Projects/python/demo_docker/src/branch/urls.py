from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token
from branch.views import BranchListCreateAPIView, BranchRetrieveUpdateDestroyAPIView, BranchListAPIView


urlpatterns = [
	path('', BranchListCreateAPIView.as_view()),
	path('<int:pk>', BranchRetrieveUpdateDestroyAPIView.as_view()),

]
