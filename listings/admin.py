from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
	list_display = ("id", "title", "is_published", "price", "sqft", "realtor")
	list_display_links = ("id", "title", "price", "sqft", "realtor")
	list_filter = ("title", "realtor")
	list_editable = ("is_published",)
	search_fields = ("title", "bedrooms")
	list_per_page = 25


admin.site.register(Listing, ListingAdmin)
