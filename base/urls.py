from django.urls import path
from .views import TaskUpdateView, TaskDeleteView, TaskListView
from users.views import CompletedUpdateView
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='todo-home'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='task-update'),
    path('task/<int:pk>/update_complete/', CompletedUpdateView.as_view(), name='complete-update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete')
]