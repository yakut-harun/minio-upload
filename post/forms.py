from django import forms

from post.models import Post


class PostForm(forms.ModelForm):
    image = forms.FileField(required=False)

    class Meta:
        model = Post
        fields = [
            'title',
            'image',
        ]
