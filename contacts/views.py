from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contacts

def contact (request):
    if request.method =="POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        contact = Contacts(listing = listing, listing_id = listing_id,name = name,email = email, phone = phone,message = message,
        user_id = user_id) #we creating object from a class with properties we just collected from the post request

        contact.save () #the obj has a method 

        #send email
        send_mail("Property listing inquiry",
        "There has been inqury for" +listing +" Sign in admin",
        "sergunshtein@gmail.com",
        [email],
        fail_silently = False
        )

        messages.success(request,"fuck off")

        return redirect("/listings/"+listing_id)
