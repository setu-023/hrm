from django.urls import path

from employee.views import EmployeeListCreateAPIView


urlpatterns = [
	path('', EmployeeListCreateAPIView.as_view(),),

]
