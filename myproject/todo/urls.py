from django.urls import path
from .views import TodoListCreateAPIView, TodoRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('api/todos/', TodoListCreateAPIView.as_view(), name='todo-list-create'),
    path('api/todos/<int:pk>/', TodoRetrieveUpdateDestroyAPIView.as_view(), name='todo-retrieve-update-destroy'),
]
