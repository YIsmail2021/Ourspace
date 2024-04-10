import socket
import secrets
from django.db import models

def generate_default_id():
    return secrets.token_urlsafe(8)

class BaseModel(models.Model):
    # anonymous user ids
    id = models.CharField(primary_key=True, max_length=16, unique=True, default=generate_default_id)

    class Meta:
        abstract = True

    @classmethod
    def get_and_save_ip(cls):
        ip_address = socket.gethostbyname(socket.gethostname())
        if ip_address:
            instance = cls(ip_address=ip_address)
            instance.save()
            return instance

class User(BaseModel):
    # in a real world scenario, would be able to view the ip address of 
    # a user.
    ip_address = models.CharField(max_length=15, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id

class Category(BaseModel):
    name = models.CharField(max_length=20)
    type = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(BaseModel):
    title = models.CharField(max_length=15)
    body = models.CharField(max_length=300)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(BaseModel):
    title = models.CharField(max_length=15)
    body = models.CharField(max_length=300)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author} on '{self.post}'"
