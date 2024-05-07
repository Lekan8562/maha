from django.urls import path

from .views import post_detail,post_comment,post_reply

app_name = 'blog'

urlpatterns = [
    path('<slug:post_slug>/',post_detail,name='post_detail'),
    path('comment/<int:post_id>/',post_comment,name='post_comment'),
    path('reply/<int:comment_id>/',post_reply,name='post_reply')
]