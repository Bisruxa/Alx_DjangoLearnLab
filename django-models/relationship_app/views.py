from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book, Author, Librarian
from .models import Library


def list_books(request):
 books =Book.objects.all()
 return render(request, 'relationship_app/list_books.html', {'book': books})
class LibraryDetailView(DetailView):
  model = Book
  template_name = 'relationship_app/library_detail.html'
  def get_contex_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    library = self.objects.all()
    context['name'] = library
    return context
