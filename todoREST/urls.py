from django.urls import include, path

from django.urls import  path
from rest_framework import routers
from .views import TaskView


urlpatterns = [
   path('', TaskView.as_view()),
   path('<int:id>/', TaskView.as_view()),
]