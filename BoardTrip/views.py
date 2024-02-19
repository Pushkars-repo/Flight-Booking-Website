from django.shortcuts import render,redirect, HttpResponse
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Flight


def index(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def flight_detail_page(request):
        flights = Flight.objects.all()
        context ={
             'flights':flights,
        }
        return render(request, 'flight_details.html',context)
@login_required(login_url='login')
def search_flight_details(request):

    if request.method == 'POST':
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        flights = Flight.objects.filter(origin__icontains=origin, destination__icontains=destination)
        # print(origin)
        # print(destination)

        return render(request, 'flight_details.html', {'origin':origin, 'flights':flights})
    else:
        return render(request, 'flight_details.html', {'origin':origin, 'flights':flights})


@login_required(login_url='login')
def book_ticket(request, id):
        booked_flight = Flight.objects.get(id=id)
        context = {
            'booked_flight':booked_flight,
        }
        return render(request, 'book_ticket.html', context)


@login_required(login_url='login')
def confirm_tkt(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        context = {
               'fname':fname,
               'lname':lname,
               'email':email,
               'phone':phone
        }
    return render(request,'confirm_tkt.html', context)




# ------------------------------------------------------------ User Registration ----------------------------------------------------

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('index')