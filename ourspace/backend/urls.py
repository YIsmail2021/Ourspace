from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserViewSet, CommentViewSet, CategoryViewSet

# Create a router and register our ViewSets with it
router = DefaultRouter()
router.register(r'post', PostViewSet, basename='post')
router.register(r'user', UserViewSet, basename='user')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'comments', CommentViewSet, basename='comment')


# The API URLs are now determined automatically by the router
urlpatterns = [
    path('', include(router.urls)),
]
