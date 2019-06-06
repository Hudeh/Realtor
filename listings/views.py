from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing
from .search_field import city_choice, state_choice







def category(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:7]
    paginator = Paginator(listings, 3) 
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
    	'listings':paged_listings
    }
    return render(request, 'listing/categore.html', context)



def listing(request, pk):
	lists = get_object_or_404(Listing, pk=pk)
	context = {
	'lists': lists
	}
	return render(request, 'listing/s_list.html', context)


def search(request):
    queryset_list = Listing.objects.order_by('-list_date')
    # keywords search
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter( description__icontains=keywords)
    #city
    
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__icontains=city)

    context = { 
    'listings' : queryset_list, 
    'state_choice': state_choice,
    'city_choice': city_choice,
    'Values' : request.GET
    }
    return render(request, 'listing/search.html', context)
