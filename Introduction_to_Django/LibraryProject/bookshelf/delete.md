# delete
# Step 1: Retrieve the book instance
book_to_delete = Book.objects.get(title="1984")

# Step 2: Delete the instance
book_to_delete.delete()
