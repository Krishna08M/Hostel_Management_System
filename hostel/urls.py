from django.urls import path
from . import views

urlpatterns = [
    path('create_room/', views.create_room, name='create_room'),
    path('register_student/', views.register_student, name='register_student'),
    path('login/', views.login_view, name='login'),
]
