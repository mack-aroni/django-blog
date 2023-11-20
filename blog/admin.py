from django.contrib import admin
from blog.models import Category, Comment, Post

class CategoryAdmin(admin.ModelAdmin):
  pass

class PostAdmin(admin.ModelAdmin):
  pass

class CommentAdmin(admin.ModelAdmin):
  pass

# registers models with the  admin classes
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)