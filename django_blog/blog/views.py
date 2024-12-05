from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,CommentForm
from .models import Profile,Tag
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.db import IntegrityError
from .forms import PostForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Comment
from django.db.models import Q


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()  # Create an empty form instance
        context['comments'] = self.object.comments.all()  # Get all comments for the post
        return context

    def post(self, request, *args, **kwargs):
        post = self.get_object()  # Correct the method name here
        form = CommentForm(request.POST)
        if form.is_valid():
            # Save the comment associated with the post and the logged-in user
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)  # Redirect back to the post detail page after saving the comment

        # If form is not valid, render the page again with the form errors
        return self.get(request, *args, **kwargs)
    
class PostCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
  model = Post
  # fields = ['title', 'content'] using both fields and form class is not allowed
  form_class = PostForm
  success_url = reverse_lazy('post_list')
  login_url = '/login/'#redirects to login page if the user is not loged in
  def test_func(self):
    return True

  def form_valid(self, form):
    form.instance.author = self.request.user
    return super().form_valid(form)
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        # Associate the comment with the current post and the logged-in user
        form.instance.author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])  # Get the post by pk
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})  # Redirect to the post detail page
class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'
    
    def get_queryset(self):
        # Ensure the user can only edit their own comments
        return self.model.objects.filter(author=self.request.user)

    def form_valid(self, form):
        # Save the form and redirect to the post detail page
        form.save()
        return redirect('post_detail', pk=self.object.post.pk)

class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'
    success_url = '/'  # Redirect to home or any other URL after successful deletion

    def get_queryset(self):
        # Ensure the user can only delete their own comments
     return self.model.objects.filter(author=self.request.user)
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
  model = Post
  fields = ['title', 'content']
  template_name = 'blog/post_form.html'
  login_url = '/login/'#redirects to login page if the user is not loged in
  success_url = reverse_lazy('post_list')
class PostDeleteView(DeleteView):
  model = Post
  template_name = 'blog/post_delete.html'
  success_url = reverse_lazy('post_list')
def search(request):
    query = request.GET.get('q')  # Get search term from query parameters

    if query:
        # Use the Q object to filter by title, content, or tags
        posts = Post.objects.filter(
            Q(title__icontains=query) |  # Filter posts where the title contains the query
            Q(content__icontains=query) |  # Filter posts where the content contains the query
            Q(tags__name__icontains=query)  # Filter posts where the tag contains the query (using taggit)
        ).distinct()  # `distinct()` ensures no duplicates if multiple conditions match
    else:
        posts = Post.objects.all()  # If no query, return all posts

    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})