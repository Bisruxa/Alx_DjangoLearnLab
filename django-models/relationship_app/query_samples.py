from .models import Book, Library, Librarian 
book = Book.objects.filter(author="").first() 
library = Library.objects.get(name=library_name)
books = library.books.all()  
for book in books:
    print(book)


librarians = Librarian.objects.all()  


for librarian in librarians:
    print(librarian)
