from django.urls import path
from .views import TodoCreateListView, TodoDetailView, UserLoginView, UserLogoutView, UserRegistrationViewset

urlpatterns = [
    path('register/', UserRegistrationViewset.as_view(), name='register'),
    path('login/',UserLoginView.as_view(), name='login'),
    path('logout/',UserLogoutView.as_view(), name='logout'),
    path('todos/', TodoCreateListView.as_view(), name='todo-list-create'),
    path('todos/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
]