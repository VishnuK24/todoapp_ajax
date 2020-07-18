"""todo urls"""

from django.urls import path
from .import views

app_name = 'todo'

urlpatterns = [
    path('todo-list', views.TodoListView.as_view(), name='todo-list'),

    path('<str:id>/completed/', views.TodoCompleteView.as_view(), name='todo-completed'),

    path('<str:id>/deleted/', views.TodoDeletedView.as_view(), name='todo-deleted')
]