from django.urls import path
from . import views 

urlpatterns = [
    path('login/',views.login_view,name = 'login'),
    path('register/',views.register_view,name='register'),
    path('logout/',views.logout_view,name ='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('post/',views.PostListView.as_view(),name = 'post_list'),
    # path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
     path('post/new/', views.PostCreateView.as_view(), name='post_create'),
     path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
     path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
     path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
  
]
