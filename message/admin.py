from django.contrib import admin
from .models import ContactForm



class ContactFormAdmin(admin.ModelAdmin):
    list_display = ("id", "listing", "email", "contact_date")
    list_display_links = ("id",  "listing")
    list_filter = ("name", "listing")
    list_per_page = 25


admin.site.register(ContactForm, ContactFormAdmin)


