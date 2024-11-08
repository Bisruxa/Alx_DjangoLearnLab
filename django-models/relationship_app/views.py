from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Author, Library, Librarian

def storage(request):
 books =Book.objects.all()
 return render(request, 'list_books.html', {'book': books})
class viewss(DetailView):
  model = Book
  template_name = 'library_detail.html'
  def get_contex_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    library = self.objects.all()
    context['name'] = library
    return context
