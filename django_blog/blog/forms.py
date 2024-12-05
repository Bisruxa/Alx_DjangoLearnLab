from django import forms
from .models import Profile,Post,Comment,Tag
from taggit.forms import TagWidget

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio']

class PostForm(forms.ModelForm):
    # tags = forms.CharField(max_length=255, required=False, help_text="Comma separated tags")
    tags = forms.CharField(widget=TagWidget()) 
    class Meta:
        model = Post
        fields = ['title', 'content','tags']
    # def save(self, commit=True):
    #     post = super().save(commit=False)
    #     if commit:
    #         post.author= self.instance.author
    #         post.save()
    #     return post
    def clean_tags(self):
        tag_names = self.cleaned_data['tags'].split(',')
        tag_objects = []
        for tag_name in tag_names:
            tag_name = tag_name.strip()
            if tag_name:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                tag_objects.append(tag)
        return tag_objects
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']