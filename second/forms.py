from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label='title', max_length=200)
    contents = forms.CharField(label='contents', widget = forms.Textarea)

