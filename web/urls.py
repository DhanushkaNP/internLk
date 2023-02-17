from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student-register', views.studentRegister, name='studentRegister'),
    path('com-register', views.comRegister, name='comRegister'),
    path('login', views.login, name='login'),
    path('homeStudent', views.homeStudent, name='homeStudent'),
    path('homeCompany', views.homeCompany, name='homeCompany'),
    path('log_out', views.log_out, name='log_out'),
    path('company-portal', views.company_portal, name='company_portal'),
    path('search-result', views.search_result, name='search_result'),
    path('remove', views.remove, name='remove')
]
