from django.urls import path

from . import views

app_name = 'testsystem'
urlpatterns = [
    path('', views.index),
    path('index/', views.index,name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('info/', views.info, name='info'),
    path('<int:paper_id>/', views.paper, name='paper'),
    path('checkin/', views.checkin, name='checkin'),
    path('<int:paper_id>/cal/', views.cal_score, name='calculate'),
    path('forgetpwd/',views.forgetpwd,name='forgetpwd'),
    path('brokenline/', views.brokenline, name='brokenline'),
    path('pie/',views.pie,name='pie'),
    path('histogram/', views.histogram, name='histogram'),
    path('download/',views.download,name='download')
]
