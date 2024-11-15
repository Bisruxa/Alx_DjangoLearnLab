# bookshelf/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        permissions = [
            ("can_create", 'Can create book'),
            ("can_delete", 'Can delete book'),
            ("can_edit", 'Can edit book'),
            ("can_view", 'Can view book'),
        ]

    def __str__(self):
        return self.title
