from django.urls import path

from storeApp import views

app_name = 'storeApp'
urlpatterns = [
    path('', views.Home, name='Home'),
    path('<slug:c_slug>/', views.department_detail, name='details'),

]
