from django.db import models
from django.urls import reverse
# Create your models here.

class Image(models.Model):
    caption = models.CharField(max_length=200,null=True,blank=True)
    image = models.ImageField(upload_to='images/project_images/')
    project = models.ForeignKey('Project',on_delete=models.CASCADE,related_name='project_images')

    def __str__(self):
        return self.caption
    

class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Project(models.Model):
    category = models.ForeignKey(Category,related_name='category_projects',on_delete=models.CASCADE,null=True)
    languages = models.ManyToManyField(Language,related_name='language_projects')
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('portfolio:project_detail', kwargs={'project_slug':self.slug})

    def __str__(self):
        return self.name

class ProjectComment(models.Model):
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='project_comments')
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    website = models.URLField(null=True,blank=True)
    email = models.EmailField()
    message = models.TextField()
    
    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Project Comments'

    def __str__(self):
        return f'{self.message[:50]} on "{self.project}"'
    
class ProjectReply(models.Model):
    comment = models.ForeignKey(ProjectComment,on_delete=models.CASCADE,related_name='project_comment_replies')
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    website = models.URLField(null=True,blank=True)
    email = models.EmailField()
    message = models.TextField()
    
    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Comment Replies'

    def __str__(self):
        return f'{self.message[:50]} on "{self.comment}"'
    
