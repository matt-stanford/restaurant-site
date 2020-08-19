from django.shortcuts import render
from .forms import ContactForm

def index(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, 'pages/index.html', {'form': form})

def about(request):
    return render(request, 'pages/about.html')
