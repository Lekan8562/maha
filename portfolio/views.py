from django.shortcuts import render,get_object_or_404,redirect

from blog.models import Post

from .models import Project,ProjectComment
from .forms import ProjectCommentForm,ProjectReplyForm

# Create your views here.

def home(request):
    projects = Project.objects.all()
    posts = Post.objects.all()
    context = {'projects':projects,'posts':posts}
    return render(request,'portfolio/home.html',context)

def project_detail(request, project_slug):
    project = get_object_or_404(Project, slug__iexact=project_slug)
    context = {'project':project}
    return render(request,'portfolio/project_detail.html',context)

def project_comment(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    comment = None
    form = ProjectCommentForm(data=request.POST)
    if request.method == 'POST':
        comment = form.save(commit=False)
        comment.project = project
        comment.save()
        return redirect(request.META.get('HTTP_REFERER'))
    return render(request,'portfolio/project_detail.html',{'project':project,'form':form,'comment':comment})

def project_reply(request, comment_id):
    comment = get_object_or_404(ProjectComment, id=comment_id)
    reply = None
    form = ProjectReplyForm(data=request.POST)
    if request.method == 'POST':
        reply = form.save(commit=False)
        reply.comment = comment
        reply.save()
        project = comment.project
        return redirect('portfolio:project_detail', project_slug=project.slug)
    else:
        form = ProjectReplyForm()
    return render(request,'portfolio/project_reply.html',{'comment':comment,'reply':reply,'form':form})
