from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Customer, Company, Marketing, Website
from .forms import CustomerForm, CompanyForm, MarketingForm, WebsiteForm

# Create your views here.
def singup(request):
    context = {

    }
    return render(request, 'singup.html', context)


def dentist(request):
    context = {

    }
    return render(request, 'request.html', context)

def customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
           
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html', {'form': form})



def website(request):
    if request.method == 'POST':
        form = WebsiteForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = WebsiteForm()
    return render(request, 'website.html', {'form': form})

def patient_password(request):
    context = {

    }
    return render(request, 'patient_password.html', context)

def patient_profile(request):
    context = {

    }
    return render(request, 'patient_profile.html', context)



def marketing(request):
    if request.method == 'POST':
        form = MarketingForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = MarketingForm()
    return render(request, 'marketing.html', {'form': form})
    

def company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = CompanyForm()
    return render(request, 'company.html', {'form': form})