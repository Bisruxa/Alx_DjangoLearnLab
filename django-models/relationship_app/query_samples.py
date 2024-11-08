from .models import Book, Library, Librarian,Author
author = Author.objects.get(name=author_name) 
Book.objects.filter(author=author)

library = Library.objects.get(name=library_name)
books = library.books.all()  
for book in books:
    print(book)


librarians = Librarian.objects.all()  


for librarian in librarians:
    print(librarian)
