"""
URL configuration for DRFProjectDemo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from DEFProjectDemoApp import views

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register('api/viewsetemployees',views.EmployeeViewSet),
router.register('api/viewsetdepartmets',views.DepartmentsViewSet),
router.register('api/viewsetcountries',views.CountriesViewSet),

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('get-api-auth-token/',obtain_auth_token, name='api_auth_token'),
    path('departments_list', views.departments_list, name='departments_list'),
    path('country_list', views.countries_list, name='countries_list'),

]

'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('api/fbvemployees/',views.Employee_list),
    path('api/fbvemployees/<int:pk>', views.Employee_detail),
    path('api/cbvemployees/', views.employelist.as_view()),
    path('api/cbvemployees/<int:pk>', views.employeedetail.as_view()),
    path('api/mixinemployees/', views.EmployeesList.as_view()),
    path('api/mixinemployees/<int:pk>', views.EmployeesDetail.as_view()),

]
'''