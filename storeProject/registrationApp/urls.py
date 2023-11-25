from django.urls import path, include

from . import views

app_name = 'register'
urlpatterns = [
   path('register', views.register, name='register'),
   path('login', views.login, name='login'),
   path('logout', views.logout, name='logout'),
   path('createorder', views.CreateOrder, name='createorder'),
   path( 'ajax/load-courses/', views.load_courses, name='ajax_load_courses')
]
