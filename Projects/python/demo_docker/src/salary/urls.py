from django.urls import path

from salary.views import SalaryListCreateAPIView, SalaryRetrieveUpdateDestroyAPIView, SalaryListAPIView, GetSalaryAPIView


urlpatterns = [
	path('', SalaryListCreateAPIView.as_view(),),
	path('<int:pk>/', SalaryRetrieveUpdateDestroyAPIView.as_view(),),
	path('show', SalaryListAPIView.as_view(),),
	path('addition', GetSalaryAPIView.as_view(),),



]
