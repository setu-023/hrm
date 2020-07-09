"""hrm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.decorators.csrf import csrf_exempt

from django.contrib import admin
from django.urls import path, include
from account.views import UserListCreateAPIView, UserLogin, PasswordSet, ChangePassword, AccountListAPIView


from base import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('homepage/', views.homePage),

    

    path('employee/', include('employee.api.urls')),
    path('department/', include('department.urls')),
    path('branch/', include('branch.urls')),
    path('dept_branch/', include('branch.urls')),
    path('salary/', include('salary.urls')),
    path('project/', include('project.urls')),
    path('project-detail/', include('projec_detail.urls')),


   
    
    
    path('account/', UserListCreateAPIView.as_view(), name='user-list-create-api'),
	path('account/show', AccountListAPIView.as_view(), name='user-list-create-api'),
    path('account/login', UserLogin.as_view(), name='user-login-`api'),
    path('account/passwordset', PasswordSet.as_view(),),
    path('account/passwordreset', ChangePassword.as_view(), name='password-reset-`api'),

    
]
