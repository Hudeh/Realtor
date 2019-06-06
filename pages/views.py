from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from listings.models import Listing
from listings.models import Realtor
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .search_field import city_choice, state_choice




def home(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:9]
    queryset_list = Listing.objects.order_by('-list_date')
    # keywords search
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)
    #city

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    context = {
        'listings': queryset_list,
        'state_choice': state_choice,
        'city_choice': city_choice,
        'Values': request.GET
    }
    return render (request, 'pages/home.html', context)


def about(request):
    # get realtor for about page
    realtors = Realtor.objects.all()
    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)
    context = {
    'realtors' : realtors,
    'mvp_realtor': mvp_realtor
    }

    return render(request, 'pages/about.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'you have login')
            return redirect('index')
        
        else:
            messages.error(request, 'you have not register')
            return redirect('login')
           
    else:
        return render(request, 'pages/login.html', {})

def register(request):
    
    if request.method == 'POST' :
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password= request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if password == password2 :

           if User.objects.filter(username=username).exists():
                    messages.error(request, 'usernam has been taken')
                    return redirect('register')
           else:
                 if User.objects.filter(email=email).exists():
                        messages.error(request, 'email already exists')
                        return redirect('register')
                 else:
                     user = User.objects.create_user(username=username, email=email, password=password, 
                     first_name=first_name, last_name=last_name)
                     user.save()
                     messages.success(request, 'you have registerd')
                     return redirect('login')
        else:
            messages.error(request, 'password do not match')
            return redirect('register')
    else:
        return render(request, 'pages/register.html', {})

   
def logout_user(request):
    logout(request)
    messages.success(request, 'you have logout')
    print('logout')
    return render(request, 'pages/login.html', {})
        


def dashboard(request):
    return render(request, 'pages/dashb.html', {})


def location(request):
    listings = Listing.objects.order_by('-list_date').filter(locations='lagos')[:1]
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        'listings': listings,
        'listings': paged_listings
    }
    return render(request, 'listing/lagos.html', context)

def location_2(request):
    listings = Listing.objects.order_by('-list_date').filter(locations='abuja')[:20]
    paginator = Paginator(listings, 3)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context ={
        'listings': listings,
        'listings': paged_listings
    }
    return render(request, 'listing/lagos.html', context)

#work on more locations page

