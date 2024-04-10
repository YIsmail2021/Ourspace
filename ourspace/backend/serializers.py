from rest_framework import serializers

from .models import Category, Post, User, Comment

def create_user(self, validated_data):
    # Check if the IP address is provided in the request data
    ip_address = self.context['request'].META.get('REMOTE_ADDR', None)
    validated_data['author'] = User.objects.create(ip_address=ip_address)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'ip_address',
            'created_on',
        ]

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'type',
        ]

class PostSerializer(serializers.ModelSerializer):
    # generated in the model.
    created_on = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'body',
            'created_on',
        ]

    def create(self, validated_data):
        # random user will be generated
        create_user(self, validated_data)
        return super().create(validated_data)

class CommentSerializer(serializers.ModelSerializer):
    # generated in the model.
    created_on = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'title',
            'body',
            'post',
            'created_on',
        ]
    
    def create(self, validated_data):
        # random user will be generated
        create_user(self, validated_data)
        return super().create(validated_data)
