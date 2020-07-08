from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from project.views import ProjectListCreateAPIView, ProjectRetrieveUpdateDestroyAPIView, ProjectCreateAPIView

app_name = 'account'

urlpatterns = [
	path('', ProjectListCreateAPIView.as_view()),
	path('<int:pk>', ProjectRetrieveUpdateDestroyAPIView.as_view()),
    path('project-detail', ProjectCreateAPIView.as_view()),


]
