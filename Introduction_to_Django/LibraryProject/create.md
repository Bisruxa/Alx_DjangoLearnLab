# Create Book Instance
```python
from bookshelf.models import Book  # Import the Book model

# Create a new Book instance
new_book = Book(title="1984", author="George Orwell", publication_year=1949)

  # Save the instance to the database
# retrieve book
retrived_book = Book.objects.get(title="1983")                
retrived_book.save()  
# update 
retrieved_book.title = '1984'
retrieved_book.save()  
#delete
retrieved_book.delete()