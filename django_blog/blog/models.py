from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
class Post(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  published_date = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  # created_at = models.DateTimeField(auto_now=True)
  tags =  TaggableManager() 
  
  
  def __str__(self):
    return self.title
class Profile(models.Model):
  user =models.OneToOneField(User,on_delete= models.CASCADE)
  bio = models.TextField(blank = True)
  location = models.CharField(max_length=100,blank =True)
  posts = models.ManyToManyField(Post, related_name= 'profile',blank =True)
  def __str__(self):

    return self.user.username
class Comment(models.Model):
  post = models.ForeignKey(Post ,related_name=
  'comments', on_delete=models.CASCADE)
  author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
  content = models.TextField(max_length=200)
  created_at = models.DateTimeField(auto_now = True)
  updated_at = models.DateTimeField(auto_now_add = True)
  def __str__(self):
    return f'Comment by {self.author.username} on {self.post.title}'
