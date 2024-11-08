from django.urls import path
from . import views
urlpatterns = [
  path('', views.storage, name='index'),
  path('detail/<int:book_id>', views.detail, name='detail'),
]
