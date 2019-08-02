from django.shortcuts import render, redirect,get_object_or_404
from .models import Newsletter,Blogs



 
def newsletter(request):
    if request.method == 'POST':
    newsemail = request.POST.get('newsemail')
    letter = Newsletter(newsemail=newsemail)
    letter.save()
    print('it works')
    return redirect('index')


def blog(request,pk):
    blogging = get_object_or_404(Blogs, pk=pk)
    context = {
        'blogging':blogging,
    }

    return render (request, 'pages/blog.html', context)