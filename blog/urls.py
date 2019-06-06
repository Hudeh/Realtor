from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^blogs/(?P<pk>[0-9]+)/$', views.singleblog, name='blogs'),
	url(r'^blog/', views.blog, name='blog')
]
