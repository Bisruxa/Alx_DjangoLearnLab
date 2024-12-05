from django import forms
from .models import Profile,Post

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
    # def save(self, commit=True):
    #     post = super().save(commit=False)
    #     if commit:
    #         post.author= self.instance.author
    #         post.save()
    #     return post