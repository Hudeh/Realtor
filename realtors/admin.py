from django.contrib import admin
from .models import Realtor

class RealtorAdmin(admin.ModelAdmin):
	list_display = ("id", "name", "phone", "email")
	list_display_links = ("id", "name", "phone", "email")
	search_fields =("name",)
	list_per_page = 10


admin.site.register(Realtor , RealtorAdmin)
