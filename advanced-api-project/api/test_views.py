from rest_framework.test import APIRequestFactory
from .models import Book,Author
from .serializers import BookSerializer
from rest_framework.test import APITestCase
from rest_framework import status


class BookTests(APITestCase):
  def setUp(self):
    author = Author.objects.create(name="J.R.R. Tolkien")
    Book.objects.create(title="The Lord of the Rings", publication_year=1954, author=author)
    

  def test_get_books(self):
    response = self.client.get('/api/books/')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(len(response.data), 1)
  def test_create_book(self):
   
   data = {
            'title': 'The Silmarillion',
            'publication_year': 1977,
            'author': self.author.id  }
   response = self.client.post('/api/books/', data, format='json')

   self.assertEqual(response.status_code, status.HTTP_201_CREATED)
   self.assertEqual(response.data['title'], data['title'])
   self.assertEqual(response.data['author'], data['author'])
   self.assertEqual(Book.objects.count(), 2)  
