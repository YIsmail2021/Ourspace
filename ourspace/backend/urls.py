from django.urls import path, include 

from .views import ListPostAPIView, CreateUserAPIView, TestView, ListUserAPIView

urlpatterns = [
    path('latest-posts/', ListPostAPIView.as_view()),
    path('create-users/', CreateUserAPIView.as_view()),
    path('list-users/', ListUserAPIView.as_view()),
    path('test-view/', TestView.as_view()),
]
