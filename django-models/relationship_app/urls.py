from django.urls import path
from .views import list_books, LibraryDetailView
urlpatterns = [
  path('', list_books, name='index'),
  path('detail/<int:book_id>', LibraryDetailView.as_view(), name='detail'),
]
