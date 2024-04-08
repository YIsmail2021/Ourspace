import socket
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# User info
class User(models.Model):
    id = models.CharField(primary_key=True, max_length=8, unique=True)
    ip_address = models.CharField(blank=True)  # Assuming IPv4 address
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class meta:
        ordering = ('username',)
    
    @classmethod
    def get_and_save_ip(cls):
        # Get the IP address of the machine
        ip_address = socket.gethostbyname(socket.gethostname())
        if ip_address:
            # Create an instance of YourModel and save the IP address
            instance = cls(ip_address=ip_address)
            instance.save()
            return instance

# Category of posts
class Category(models.Model):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class meta:
        ordering = ('name',)

# Post info
class Post(models.Model):
    title = models.CharField(max_length=15)
    body = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    class meta:
        ordering = ('created_on',)

# Comments of posts, written by users
class Comment(models.Model):
    title = models.CharField(max_length=15)
    body = models.CharField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.author} on '{self.post}'"

    class meta:
        ordering = ('created_on',)
