from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^contact/', views.contacts, name='contact'),
]