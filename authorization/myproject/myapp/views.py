from email.message import EmailMessage

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from myproject import settings
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from . tokens import generate_token

def home(request):
    return render(request, 'myapp/index.html')

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "username already exists! please try some other username")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "email already registered")
            return redirect('home')

        if len(username)>10:
            messages.error(request, "username should be within 10 characters")

        if pass1 != pass2:
            messages.error(request, "password didn't match")

        if not username.isalnum():
            messages.error(request, "username must be alphanumeric")
            return redirect('home')



        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False
        myuser.save()

        messages.success(request, "Your account created successfully")

# welcome Email
        subject = "Welcome to MCS"
        message = "Hello" + myuser.first_name + "!! \n" + "Welcome to MCS"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently = True)

# Email address Confirmation mail

        current_site = get_current_site(request)
        email_subject = "Confirm Your Email @ authorization . Django Login!!"
        message2 = render_to_string('email_confirmation.html',{
            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser),
        })

        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],

        )
        email.fail_silently = True
        email.send()



        return redirect('signin')


    return render(request,'myapp/signup.html')

def signin(request):

    if request.method=='POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username = username, password = pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "myapp/index.html", {'fname': fname})
        else:
            messages.error(request, 'Bad Credentials')
            return redirect('home')


    

    return render(request,'myapp/signin.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect('home')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    else:
        return render(request, 'activation_failed.html')





