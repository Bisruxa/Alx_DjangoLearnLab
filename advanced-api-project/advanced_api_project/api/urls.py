from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import Bookviewset,Authorviewset
router = DefaultRouter()
router.register(r"books",Bookviewset)
router.register(r"authors",Authorviewset)
urlpatterns = [
  path("",include(router.urls)),
]