from django.shortcuts import render, get_object_or_404,redirect

from .models import Post,PostComment
from .forms import PostCommentForm,PostReplyForm
# Create your views here.

def post_detail(request,post_slug):
    post = get_object_or_404(Post, slug__iexact=post_slug)
    context = {'post':post}
    return render(request,'post/post_detail.html',context)

def post_comment(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    comment = None
    form = PostCommentForm(data=request.POST)
    if request.method == 'POST':
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect(request.META.get('HTTP_REFERER'))
    return render(request,'post/post_detail.html',{'post':post,'comment':comment,'form':form})


#COMMENT REPLIES FOR POST
def post_reply(request, comment_id):
    comment = get_object_or_404(PostComment, id=comment_id)
    reply = None
    form = PostReplyForm(data=request.POST)
    if request.method == 'POST':
        reply = form.save(commit=False)
        reply.comment = comment
        reply.save()
        post = comment.post
        return redirect('blog:post_detail', post_slug=post.slug)
    else:
        form = PostReplyForm()
    return render(request,'post/post_reply.html',{'comment':comment,'reply':reply,'form':form})
