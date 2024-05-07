from django import forms

from .models import PostComment,PostReply

class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['name','website','email','message']

class PostReplyForm(forms.ModelForm):
    class Meta:
        model = PostReply
        fields = ['name','website','email','message']

        