from django.urls import path

from activity.views import ActivityListCreateAPIView, ActivityRetrieveUpdateDestroyAPIView, ActivityListAPIView


urlpatterns = [
	path('', ActivityListCreateAPIView.as_view(),),
	path('<int:pk>/', ActivityRetrieveUpdateDestroyAPIView.as_view(),),
	path('show', ActivityListAPIView.as_view(),),

	# path('addition', GetSalaryAPIView.as_view(),),



]
