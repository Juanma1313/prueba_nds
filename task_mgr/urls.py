from django.urls import path
from . import views


urlpatterns = [
    path('register_user/', views.register_user, name='register_user'),
    path("create_task/", views.create_task, name="create_task"),
]
