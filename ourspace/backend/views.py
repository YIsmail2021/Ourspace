from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from .models import User, Post
from .serializers import PostSerializer, UserSerializer

# TODO: Convert to class based views.
class ListPostAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
class CreateUserAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListUserAPIView(ListAPIView):
    queryset = Post.objects.all().order_by('created_on')
    serializer_class = UserSerializer

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        return Response('Hello')