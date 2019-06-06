from django.shortcuts import render, get_object_or_404
from .models import Blog


def blog(request):
    blogg = Blog.objects.order_by("-list_date").filter(is_published=True)[:9]
    context = {
        'blogg':blogg
    }
    if request.method=='POST':
        names= request.POST.get('names')
        email= request.POST.get('email')
        message= request.POST.get('mesage')

    return render(request, 'pages/blog.html', context)


def singleblog(request, pk):
    blogs = get_object_or_404(Blog, pk=pk)
    context = {
        'blogs':blogs
    }
    return render(request,'pages/s_blog.html', context)