from django.urls import path

from employee.views import EmployeeListCreateAPIView, EmployeeRetrieveUpdateAPIView, EmployeeListAPIView


urlpatterns = [
	path('', EmployeeListCreateAPIView.as_view(),),
	path('<int:pk>/', EmployeeRetrieveUpdateAPIView.as_view(),),
	path('show', EmployeeListAPIView.as_view(),),


]
