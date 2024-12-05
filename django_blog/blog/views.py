from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.db import IntegrityError
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

def register_view(request):
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
     try:
      form.save()
      return redirect('login')
     except IntegrityError:
      form.add_error('username', 'Username already exists')

    else:
     form.add_error('username', 'there was an issue with the username')

     return render(request,'blog/register.html',{"form": form})
      
    
    
  else:
    form = UserCreationForm()
    context = {'form':form}
    return render(request,'blog/register.html',context)
def login_view(request):
  if request.method == "POST":
   form = AuthenticationForm(data = request.POST)
   if form.is_valid():
    login(request,form.get_user())
    return redirect('profile')
   else:
     messages.error(request,"Invalid username or password")
  else:
    form = AuthenticationForm()
  return render(request,'blog/login.html',{"form": form})

def logout_view(request):
  logout(request)
  return redirect('login')
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

@login_required
def profile_view(request):
    # Retrieve the user's profile or create one if it doesn't exist
    # profile = Profile.objects.get_or_create(user=request.user)

    # if request.method == 'POST':
    #     form = ProfileForm(request.POST, instance=profile)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('profile')  # Redirect to the profile page after saving
    # else:
    #     form = ProfileForm(instance=profile)

    # return render(request, 'profile.html', {'form': form})
    profile , created = Profile.objects.get_or_create(user=request.user)
    return render(request, 'blog/profile.html', {'profile': profile})
class PostListView(ListView):
  model = Post
  template_name = 'blog/post_list.html'
  context_object_name = 'posts'
class PostDetailView(DetailView):
  model = Post
  template_name = 'blog/post_detail.html'
  context_object_name = 'post'  

class PostCreateView(LoginRequiredMixin,CreateView):
  model = Post
  # fields = ['title', 'content'] using both fields and form class is not allowed
  form_class = PostForm
  success_url = reverse_lazy('post_list')
  login_url = '/login/'#redirects to login page if the user is not loged in

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UpdateView):
  model = Post
  fields = ['title', 'content']
  template_name = 'blog/post_form.html'
  login_url = '/login/'#redirects to login page if the user is not loged in
  success_url = reverse_lazy('post_list')
class PostDeleteView(DeleteView):
  model = Post
  template_name = 'blog/post_delete.html'
  success_url = reverse_lazy('post_list')
