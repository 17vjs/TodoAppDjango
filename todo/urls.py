from django.urls import include, path

from . import views
from django.urls import  path
from . import views


app_name = "todo"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:task_id>/", views.task, name="task"),
    path("<int:task_id>/actions/", views.actions, name="task_actions"),
    path("create_task/", views.task, name="create_task"),
    path("add/", views.actions, name="add"),
]