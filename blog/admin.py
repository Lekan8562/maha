from django.contrib import admin

from .models import Post,BlogCategory,Tag,PostComment

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(BlogCategory)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(PostComment)
