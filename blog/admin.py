from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ['title', 'content']
    list_filter = ('created_at', 'author')
    ordering = ('-created_at',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)