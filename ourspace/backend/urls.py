from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserViewSet, CommentViewSet, CategoryViewSet, PostCommentsAPIView

# Create a router and register our ViewSets with it
router = DefaultRouter()
router.register(r'post', PostViewSet, basename='post')
router.register(r'user', UserViewSet, basename='user')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'comments', CommentViewSet, basename='comments')


urlpatterns = [
    path('', include(router.urls)),
    path('post-comments/<str:pk>/', PostCommentsAPIView.as_view(), name='post-comments'),
]
