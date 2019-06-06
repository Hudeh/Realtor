from django.urls import path
from . import views


urlpatterns =   [
	path('', views.home, name='index'),
	path('login/', views.login_user, name='login'),
	path('register/', views.register, name='register'),
	path('about/', views.about, name='about'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('logout/', views.logout_user, name='logout'),
    path('lagos/', views.location, name='lagos'),
	path('abuja/', views.location_2, name='abuja'),
	
]
