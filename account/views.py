from django.shortcuts import render, redirect

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
    context = {

    }
    return render(request, 'customer.html', context)



def website(request):
    context = {

    }
    return render(request, 'website.html', context)

def patient_password(request):
    context = {

    }
    return render(request, 'patient_password.html', context)

def patient_profile(request):
    context = {

    }
    return render(request, 'patient_profile.html', context)