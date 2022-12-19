from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.

def home(request):
    print("========inside home===")
    return render(request, "home.html")

def login(request):
    print("========inside login===")
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            report_loc = '../Forms/'
            return render(request,'form.html',{'loc':report_loc,'error': ''})
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('/')
    return render(request,'login.html')
def register(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('password1')
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return  redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
                user.save()
                report_loc = '..login/'
                return render(request,'login.html',{'loc':report_loc,'error': ''})

        else:
            messages.info(request,"password not Matching")
            return redirect('register')

    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def Forms(request):
    if request.method == "POST":
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        email = request.POST['email']
        address = request.POST['address']
        phonenum = request.POST['phonenum']
        if User.objects.filter( name= name).exists():
            messages.info(request, "name Taken")
            return redirect('Forms')
        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email Taken")
            return redirect('Forms')
        else:
            user=User.objects.create_user(name=name, dob= dob,  age= age,  gender= gender, email= email, address= address, phonenum= phonenum)
            user.save()
            report_loc = '../home/'
            return render(request,'home.html',{'loc': report_loc, 'error': ''})

    return render(request, 'home.html')