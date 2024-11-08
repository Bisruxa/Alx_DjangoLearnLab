from .models import Book, Library, Librarian 
book = Book.objects.filter(author="").first() 
library = Library.objects.filter(name="library_name").first()
if library:
   
    books = library.books.all()  
    
   
    for book in books:
        print(book)


librarians = Librarian.objects.all()  


for librarian in librarians:
    print(librarian)
