from django.shortcuts import render, redirect
from .models import Newsletter



 
def newsletter(request):
    if request.method == 'POST':
        newsemail = request.POST.get('newsemail')
    letter = Newsletter(newsemail=newsemail)
    letter.save()
    print('it works')
    return redirect('index')

