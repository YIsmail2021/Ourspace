from rest_framework import serializers

from .models import Category, Post, User, Comment

def create_user(self, validated_data):
    # Check if the IP address is provided in the request data
    ip_address = self.context['request'].META.get('REMOTE_ADDR', None)
    validated_data['author'] = User.objects.create(ip_address=ip_address)


class UserSerializer(serializers.ModelSerializer):
    humanize_created_on = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'ip_address',
            'humanize_created_on',
        ]
    
    def get_humanize_created_on(self, obj):
        return obj.created_on.strftime('%d-%m-%Y %H:%M')

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'type',
        ]

# TODO: Make some sort of previewed text.
class PostSerializer(serializers.ModelSerializer):
    # generated in the model.
    humanize_created_on = serializers.SerializerMethodField(read_only=True)
    author_id = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'body',
            'author_id',
            'humanize_created_on',
        ]
    
    def get_humanize_created_on(self, obj):
        return obj.created_on.strftime('%d-%m-%Y %H:%M')
    
    def get_author_id(self, obj):
        return obj.author.pk

    def create(self, validated_data):
        # random user will be generated
        create_user(self, validated_data)
        return super().create(validated_data)

class CommentSerializer(serializers.ModelSerializer):
    # generated in the model.
    humanize_created_on = serializers.SerializerMethodField(read_only=True)
    author_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'title',
            'body',
            'post',
            'humanize_created_on',
        ]
    
    def get_humanize_created_on(self, obj):
        return obj.created_on.strftime('%d-%m-%Y %H:%M')
    
    def create(self, validated_data):
        # random user will be generated
        create_user(self, validated_data)
        return super().create(validated_data)
