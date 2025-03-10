from django.urls import path
from .views import TodoCreateListView, TodoDetailView

urlpatterns = [
    path('todos/', TodoCreateListView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
]