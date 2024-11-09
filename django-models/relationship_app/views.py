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
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm
def register(request):
  form = UserCreationForm()
  context = {'form':form}
  return render(request , 'relationshi_app/register.html',context)
