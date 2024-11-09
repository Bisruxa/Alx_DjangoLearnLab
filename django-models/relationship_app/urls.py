# from django.urls import path
# from .views import list_books, LibraryDetailView
# urlpatterns = [
#   path('', list_books, name='index'),
#   path('detail/<int:book_id>', LibraryDetailView.as_view(), name='detail'),
# ]

from django.contrib.auth.views import LoginView,LogoutView
from django.urls import path

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]