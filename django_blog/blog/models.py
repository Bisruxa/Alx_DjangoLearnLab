from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  published_date = models.DateTimeField(auto_now_add=True)
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title
class Profile(models.Model):
  user =models.OneToOneField(User,on_delete= models.CASCADE)
  bio = models.TextField(blank = True)
  location = models.CharField(max_length=100,blank =True)
  posts = models.ManyToManyField(Post, related_name= 'profile',blank =True)
  def __str__(self):

    return self.user.username