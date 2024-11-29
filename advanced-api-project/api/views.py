from django.shortcuts import render
from rest_framework import viewsets
from .models import Book,Author
from .serializers import BookSerializer,AuthorSerializer
# class Bookviewset(viewsets.ModelViewSet):
#   queryset = Book.objects.all()
#   serializer_class = BookSerializer
# class Authorviewset(viewsets.ModelViewSet):
#   queryset = Author.objects.all()
#   serializer_class = AuthorSerializer
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated,AllowAny

class BookListView(ListAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes=[IsAuthenticatedOrReadOnly]

class BookCreateView(CreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes=[IsAuthenticated]
class BookDetailView(RetrieveAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes=[AllowAny]
class BookUpdateView(UpdateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes=[IsAuthenticated]
class BookDeleteView(DestroyAPIView): 
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes=[IsAuthenticated]