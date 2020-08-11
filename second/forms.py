from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
# from django import forms
#
# class PostForm(forms.Form):
#     title = forms.CharField(label='title', max_length=200)
#     contents = forms.CharField(label='contents', widget = forms.Textarea)
from second.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','contents']
        labels = {
            'title' : _('제목'),
            'contents' : _('내용'),
        }
