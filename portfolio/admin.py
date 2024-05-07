from django.contrib import admin

from .models import Project,Image,Language,Category,ProjectComment,ProjectReply
# Register your models here.
admin.site.register(Image)

admin.site.register(Language)
admin.site.register(Category)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(ProjectComment)
admin.site.register(ProjectReply)
