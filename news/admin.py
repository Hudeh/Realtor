from django.contrib import admin
from .models import Newsletter,Blogs

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('newsemail',)

admin.site.register(Newsletter, NewsletterAdmin)

class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title','is_published')
    list_display_links=('title', 'is_published')
    list_filter=('author', 'title')
admin.site.register(Blogs, BlogsAdmin)