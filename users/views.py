from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Login handler
def auth_login(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            return render(request, 'users/login.html')
        else:
            # Take them to the orders page
            return HttpResponseRedirect(reverse('index'))

    # Grab form data
    username = request.POST['username']
    password = request.POST['password']

    # Do validation
    errors = {}
    if username == "" or username is None:
        errors['username'] = "Username is required"

    if password == "" or password is None:
        errors['password'] = "Password is required"

    # Go back to the form if there were errors
    if len(errors) > 0:
        return render(request, 'users/login.html', {'errors':errors})
    
    # Otherwise login user
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)

        # Create an empty cart in session
        request.session['Cart'] = []

        # Take them to the orders page
        return HttpResponseRedirect(reverse('index')) 

    
    # Go back to login page with error message
    messages.add_message(request, messages.WARNING, 'Invalid login credentials')
    return HttpResponseRedirect(reverse('login'))
    

# Logout handler
def auth_logout(request):
    request.session['Cart'] = []
    logout(request)

    # Take them to the login page
    messages.add_message(request, messages.SUCCESS, 'You are logged out')
    return HttpResponseRedirect(reverse('login')) 


# Registration handler
def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html')
    

    # Grab form data
    username = request.POST['username']
    email = request.POST['email']
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    password = request.POST['password']
    confirm_password = request.POST['conf_password']

    # Do validation
    errors = {}
    if username == "" or username is None:
        errors['username'] = "Username is required"

    if email == "" or email is None:
        errors['email'] = "Email is required"

    if firstname == "" or firstname is None:
        errors['firstname'] = "Firstname is required"

    if lastname == "" or lastname is None:
        errors['lastname'] = "Lastname is required"

    if password == "" or password is None:
        errors['password'] = "Password is required"
    elif confirm_password == "" or confirm_password is None:
        errors['conf_password'] = "Confrim Password is required"
    elif password != confirm_password:
        errors['password'] = errors['conf_password'] = "Passwords do no match"

    # Go back to the form if there were errors
    if len(errors) > 0:
        return render(request, 'users/register.html', {'errors':errors})


    # Otherwise create user
    user = User.objects.create_user(username, email, password)
    user.firstname = firstname
    user.lastname = lastname
    user.save()

    # Take them to the login page
    messages.add_message(request, messages.SUCCESS, 'Registration Successful')
    return HttpResponseRedirect(reverse('login'))    