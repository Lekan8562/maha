from django import forms

from .models import ProjectComment,ProjectReply

class ProjectCommentForm(forms.ModelForm):
    class Meta:
        model = ProjectComment
        fields = ['name','email','website','message']

class ProjectReplyForm(forms.ModelForm):
    class Meta:
        model = ProjectReply
        fields = ['name','email','website','message']
