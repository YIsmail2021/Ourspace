from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# User info
class User(models.Model):
    username = models.CharField(max_length=15)
    first_name = models.CharField(max_length=15, blank=True)
    last_name = models.CharField(max_length=15, blank=True)
    email = models.EmailField()
    mobile_number = PhoneNumberField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username

    class meta:
        ordering = ('username',)

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
