from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^lists/(?P<pk>[0-9]+)/$', views.listing, name='listing'),
	url(r'^searched/', views.search, name='search'),
	url(r'category/', views.category, name='f_listings'),
]
