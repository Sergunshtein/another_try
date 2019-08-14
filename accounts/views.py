from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from contacts.models import Contacts  #we bringing in contact model = a dict 

def register (request):
    if request.method =='POST':
        #Get from values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        #check pswd to match
        if password==password2:
           #check username
           if User.objects.filter(username = username).exists():
                  messages.error(request,'the name is taken')
                  return redirect ('register')
           else:
                  if User.objects.filter(email = email).exists():
                      messages.error(request,'the email is taken')
                      return redirect ('register')
                  else:
                      #looks good . this is how we log the user in
                      user = User.objects.create_user(username = username,password = password,email= email,
                      first_name=first_name,last_name = last_name)
                      auth.login(request,user)
                      messages.success(request,'wellcome mothefucker')
                      return redirect('index')
                      #and thats how we let him log in by himself
                      #user.save()
                      #messages.success(request,'log the shit in ')
                      #return redirect('login')
                      



            
        

        else:
            messages.error(request,'Paswds dont match')
            return redirect ('register')


    else:
        return render(request,'accounts/register.html')

def login (request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username,password = password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'welcome dick')
            return redirect('dashboard')
        else:
            messages.error(request, "invalid dick")
            return redirect ('login')
    else:
        return render(request,'accounts/login.html')

def logout (request):
    if request.method =='POST':
        auth.logout(request)
        #message.success(request,'logged out ')
        return redirect('index')

def dashboard (request):

    #we getting only those contacts where user_id is matching request.user.id
    user_contacts = Contacts.objects.order_by('-contact_date').filter(user_id=request.user.id) 

    context = {
        'contacts':user_contacts 
    }

    return render(request,'accounts/dashboard.html',context) #why can't we simply pass user_contacts ??? 
    # but context['contacts'] will be called 
    



