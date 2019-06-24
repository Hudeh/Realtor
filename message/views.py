from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import ContactForm
import smtplib, ssl
from . import config

def contacts(request):
   #getting user message oninquiry
    if request.method == 'POST':
        listing_id = request.POST.get('listing_id')
        listing = request.POST.get('listing')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        user_id = request.POST.get('user_id')
        

        #check if user has made inquiry on the same product
        if request.user.is_authenticated:
                user_id = request.user.id
                has_contacted = ContactForm.objects.all().filter(listing_id=listing_id, user_id=user_id)
                if has_contacted:
                        messages.error(request, 'you alredy made inquiry')
                        return redirect('/listings/lists/'+listing_id)
        contact = ContactForm(name=name, email=email, phone=phone,
                              message=message, user_id=user_id, listing=listing, listing_id=listing_id)
        contact.save()
        # send mail to realtor for property inquiry


        smtp_server = "smtp.gmail.com"
        port = 465

        sender = 'classudeh@gmail.com'
        password = config.EMAIL_PASSWORD

        reciever = email
        message = """\
        From: {}
        To : {}
        Subject: python email!

        working on my python skills.

        """.format(sender,reciever)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender, password)
                server.sendmail(sender,reciever,message)
                print('it worked')
        
        return redirect('/listings/lists/'+listing_id)
