# retrieve book
retrived_book = Book.objects.get(title="1983")                
retrived_book.save()  