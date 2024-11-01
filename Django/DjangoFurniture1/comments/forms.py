# from django import forms
# from .models import Comment

# class CommentForm(forms.Form):
#     content_type = forms.CharField(widget=forms.HiddenInput)
#     object_id = forms.IntegerField(widget=forms.HiddenInput)
#     # parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
#     content = forms.CharField(widget=forms.Textarea)


from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')