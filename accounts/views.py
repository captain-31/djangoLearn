from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method == 'POST':
        # get values form the page
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')


    else:
        return render(request, 'login.html')

def register(request):

    # Check which type of request is coming, get or post & Accordingly perform the steps

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('Username Taken')
                # TO show the message on the html form, we use this format
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                # print("email taken")
                messages.info(request, 'Email exists')
                return redirect('register')
            else:
                # Add user to the user table
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('User created')
                return redirect('login')
        else:
            # print("password not matching")
            messages.info(request, 'Password not matching')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')
