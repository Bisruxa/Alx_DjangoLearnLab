from django import forms
from .models import Profile,Post,Comment,Tag
from taggit.forms import TagWidget
from django.forms import widgets
from django.contrib.auth.models import User
from .models import ProfilePicture
# can be used to add styling to our forms
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']
   


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = ProfilePicture
        fields = ('image',)
class PostForm(forms.ModelForm):
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    title = forms.CharField(widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
    content = forms.CharField(widget=widgets.Textarea(attrs={'class': 'form-control','placeholder': 'Content'}))
    tags = forms.CharField(widget=widgets.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Post
        fields = ['title', 'content','tags']
    def __init__(self, *args, request=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request
    def form_valid(self, form):
     post = form.save(commit=False)
     post.author = self.request.user
     post.save()
     tags = form.cleaned_data['tags'].split(',')
     for tag_name in tags:
        tag_name = tag_name.strip()
        if tag_name:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)
     return super().form_valid(form)   
    def save(self, commit=True, request=None):
        post = super().save(commit=False)
        if request:
            post.author = request.user  # set author to current user
        if commit:
            post.save()
        return post
    def clean_tags(self):
        tags = self.cleaned_data['tags'].split(',')
        return [tag.strip() for tag in tags if tag.strip()]
   
class CommentForm(forms.ModelForm):

    content = forms.CharField(widget=widgets.Textarea(attrs={'class': 'form-control form-control-sm ','placeholder': 'Content', 'style': 'font-size: 12px; padding: 16px; height: 80px;'  }))
    class Meta:
        model = Comment
        fields = ['content']