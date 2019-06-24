from django.contrib import admin
from .models import Newsletter

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('newsemail',)

admin.site.register(Newsletter, NewsletterAdmin)

# Register your models here.
