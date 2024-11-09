from django.db import models

# class Author(models.Model):
#   name = models.CharField(max_length = 100)
#   def __str__(self):
#     return self.name
  
# class Book(models.Model):
#   title = models.CharField(max_length =100)
#   author = models.ForeignKey(Author , on_delete = models.CASCADE)
#   def __str__(self):
#     return self.title
# class Library(models.Model):
#   name = models.CharField(max_length = 100)
#   book = models.ManyToManyField(Book)
#   def __str__(self):  
#     return self.name
# class Librarian(models.Model):
#   name = models.CharField(max_length = 100)
#   library = models.OneToOneField(Library, on_delete = models.CASCADE)
#   def __self__(self):
#     return self.name


class UserProfile(models.Model):
  ADMIN ='Admin'
  LIBRARIAN = 'Librarian'
  MEMBER='Member'

  Roles = [
    (ADMIN,'Admin'),
    (LIBRARIAN,'Librarian'),
    (MEMBER,'Member')
  ]
  role = models.CharField(max_length = 100,choices=Roles,default=MEMBER)
  user = models.OneToOneField('auth.User', on_delete = models.CASCADE)
  def __str__(self):
    return f"{self.user} - {self.role}"