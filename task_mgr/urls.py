from django.urls import path
from . import views


urlpatterns = [
    path('register_user/', views.register_user, name='register_user'),
    path("task_create/", views.task_create, name="task_create"),
    path("task_list/", views.task_list, name="task_list"),
    path("task_detail/<int:task_id>/", views.task_detail, name="task_detail"),
    path("task_update/<int:task_id>/", views.task_update, name="task_update"),
    path("task_delete/<int:task_id>/", views.task_delete, name="task_delete"),
    path("get_username", views.get_username, name="get_username"),
    path("update_profile/", views.update_profile, name="update_profile")

]
