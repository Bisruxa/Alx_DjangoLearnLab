from .models import Book,Library,Librarian 
book = Book.objects.get(author = "")
library = Library.objects.get(name = "Library Name")
books = library.book.all()
for book in books:
  print(book)
librarian =Librarian.name.all()
