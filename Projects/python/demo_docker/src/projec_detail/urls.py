from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from projec_detail.views import ProjectDetailListCreateAPIView


urlpatterns = [
	path('', ProjectDetailListCreateAPIView.as_view()),

]
