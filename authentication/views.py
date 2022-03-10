from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home(request):
    """Homepage for Stock Market"""

    return render(request, "authentication/index.html")


def signup(request):
    """Sign up form for user registration"""

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try another username.")
            return redirect('home')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered, Please login instead!!")
            return redirect('home')

        if len(username) > 20:
            messages.error(request, "Username must be under 20 characters!!")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't matched!!")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your Account has been created successfully!!")
        return redirect('signin')

    return render(request, "authentication/signup.html")


def signin(request):
    """Sign in form for user login"""

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.success(request, "Logged In Sucessfully!!")
            return render(request, "authentication/index.html", {"fname": fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')

    return render(request, "authentication/signin.html")


def signout(request):
    """Sign out for logged in user"""

    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')
