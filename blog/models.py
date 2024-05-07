from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from froala_editor.fields import FroalaField
# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def __str__(self):
        return self.name


class BlogCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    class Meta:
        verbose_name_plural = 'Blog Categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.ForeignKey(BlogCategory,related_name='category_posts',on_delete=models.CASCADE,null=True)
    tags = models.ManyToManyField(Tag,related_name='tag_posts')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    cover = models.ImageField(upload_to='post/covers/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,related_name='author_posts',on_delete=models.CASCADE)
    body = FroalaField()

    class Meta:
        ordering = ['title','-created']

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'post_slug':self.slug})

    def __str__(self):
        return self.title 


class PostComment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='post_comments')
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    website = models.URLField(null=True,blank=True)
    email = models.EmailField()
    message = models.TextField()
    
    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Post Comments'

    def __str__(self):
        return f'{self.message[:50]} on "{self.post}"'

class PostReply(models.Model):
    comment = models.ForeignKey(PostComment,on_delete=models.CASCADE,related_name='post_comment_replies')
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    website = models.URLField(null=True,blank=True)
    email = models.EmailField()
    message = models.TextField()
    
    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Post Comment Replies'

    def __str__(self):
        return f'{self.message[:50]} on "{self.comment}"'
    

