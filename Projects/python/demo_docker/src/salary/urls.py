from django.urls import path

from salary.views import SalaryListCreateAPIView, SalaryRetrieveUpdateDestroyAPIView, SalaryListAPIView


urlpatterns = [
	path('', SalaryListCreateAPIView.as_view(),),
	path('<int:pk>/', SalaryRetrieveUpdateDestroyAPIView.as_view(),),
	path('show', SalaryListAPIView.as_view(),),


]
