from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from salon.models import *
from salon.forms import *
from django.db import transaction



def home(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        contact = Contact(name=name, email=email, subject=subject, message=message)
        contact.save()
        context['message'] = f"Dear {name}, Thanks for the Review!"

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')


def booking(request):
    context = {}
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            date_str = form.cleaned_data['date']
            time = form.cleaned_data['time']
            stylist = form.cleaned_data['stylist']
            status = "Pending"

            booking = Total(name=name, email = email, phone=phone, date=date_str, time=time, stylist=stylist, status=status)
            booking.save()

            context['message'] = f"Dear {name}, Your slot has been booked!"

            return render(request, 'booking.html',context)
    
    form = BookingForm()   
    return render(request, 'booking.html', {'form': form.as_div()})


def terms(request):
    return render(request, 'tandc.html')

def privacy(request):
    return render(request, 'privacy.html')

def admin_login(request):
    context = {}
    
    if request.method == 'POST':
        username = request.POST.get("uName")
        password = request.POST.get("uPwd")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_panel')
        else:
            context['message'] = 'Invalid username or password.'
    
    return render(request, 'admin_login.html', context)

def admin_panel(request):
    pending_bookings = Total.objects.filter(status='Pending').count()
    accepted_bookings = Accepted.objects.filter(status='Accepted').count()
    rejected_bookings = Rejected.objects.filter(status='Rejected').count()

    context = {
        'pending_bookings': pending_bookings,
        'accepted_bookings': accepted_bookings,
        'rejected_bookings': rejected_bookings,
    }
    return render(request, 'admin_panel.html', context)


def pending_bookings(request):
    pending = Total.objects.all()

    context = {
        'pending': pending
    }

    return render(request, 'pending_bookings.html', context)



def accepted_bookings(request):
    accepted = Accepted.objects.all()

    context = {
        'accepted': accepted
    }

    return render(request, 'accepted_bookings.html', context)




def rejected_bookings(request):
    rejected = Rejected.objects.all()
      

    context = {
        'rejected': rejected
    }

    return render(request, 'reject_bookings.html', context)


def contact_review(request):
    contact = Contact.objects.all()

    context = {
        'contact': contact
    }

    return render(request, 'contact.html', context)

