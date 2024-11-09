# from django.shortcuts import render
# from django.views.generic.detail import DetailView
# from .models import Book
# from .models import Library

# def list_books(request):
#  books =Book.objects.all()
#  return render(request, 'relationship_app/list_books.html', {'book': books})
# class LibraryDetailView(DetailView):
#   model = Book
#   template_name = 'relationship_app/library_detail.html'
#   def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     library = self.get_object()
#     context['name'] = library
#     return context

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm
def register(request):
  form = UserCreationForm()
  context = {'form':form}
  return render(request , 'relationship_app/register.html',context)
def admin_view(request):
    
    if request.user.userprofile.role != 'Admin':
        return HttpResponse("You are not authorized to view this page.")
    return render(request, 'admin_view.html')





























# views.py
from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm  # Assuming you have a BookForm for handling the book data
from django.contrib.auth.decorators import permission_required

# View for adding a new book
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')  # Redirect to a list of books after adding
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})
# View for editing an existing book
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_detail', pk=book.pk)  # Redirect to the book details page after editing
    else:
        form = BookForm(instance=book)
    return render(request, 'edit_book.html', {'form': form})
# View for deleting a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')  # Redirect to the list of books after deleting
    return render(request, 'delete_book.html', {'book': book})
