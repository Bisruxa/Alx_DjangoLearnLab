from django.urls import path
from . import views

urlpatterns = [
  path('', views.res, name='response'),
  path('',views.res2,name="response2")
]