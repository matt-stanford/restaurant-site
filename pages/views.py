from django.shortcuts import render, redirect, get_object_or_404

from datetime import datetime

from .forms import ContactForm, EnquiryForm, CustomerForm
from .models import Reservation, Customer, MenuItem

def index(request):
    sample_menu_one = MenuItem.objects.filter(course='Main')[:3]
    sample_menu_two = MenuItem.objects.filter(course='Main')[3:6]
    form = ContactForm(request.POST or None)
    
    context = {
        'sample_menu_one': sample_menu_one,
        'sample_menu_two': sample_menu_two,
        'form': form
    }
    if form.is_valid():
        form.save()
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def menu(request):
    starters = MenuItem.objects.filter(course='Starter')
    mains = MenuItem.objects.filter(course='Main')
    sides = MenuItem.objects.filter(course='Side')
    desserts = MenuItem.objects.filter(course='Dessert')

    context = {
        'starters': starters,
        'mains': mains,
        'sides': sides,
        'desserts': desserts
    }

    return render(request, 'pages/menu.html', context)

def booking(request):
    form = EnquiryForm(request.POST or None)

    if form.is_valid():
        form.save()

        request.session['date'] = request.POST.get('date', None)
        request.session['time'] = request.POST.get('time', None)
        request.session['guests'] = request.POST.get('guests', None)

        return redirect('guest_details')

    return render(request, 'pages/booking.html', {'form': form})

def guest_details(request):
    form = CustomerForm(request.POST or None)
    date = request.session.get('date', None)
    time = request.session.get('time', None)
    guests = request.session.get('guests', None)

    context = {
        'form': form,
        'date': date,
        'time': time,
        'guests': guests
    }

    if form.is_valid():
        form.save()
        number_guests = int(guests.split(' ')[0])
        request.session['form_id'] = form.instance.id
        
        Reservation.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=date,
            time=time,
            guests=number_guests,
            form_id=form.instance.id)
        
        return redirect('booking_confirmed')
    return render(request, 'pages/guest-details.html', context)

def booking_confirmed(request):
    reservation = get_object_or_404(Reservation, form_id=request.session.get('form_id', None))
    return render(request, 'pages/booking-confirmed.html', {'reservation': reservation})