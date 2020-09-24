from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from . models import *

# Create your views here.

def index(request):
    beneficiary = Beneficiary.objects.all()[:3]
    context = {
        'testimonials': beneficiary,
    }
    return render(request, 'index.html',context)


def donor(request):
    return render(request, 'base.html')

def add_donor(request):
    obj = Donors()
    obj.firstname = request.POST['fname']
    obj.lastname = request.POST['lname']
    obj.email = request.POST['email']
    obj.address1 = request.POST['address1']
    obj.address2 = request.POST['address2']
    obj.gender = request.POST['gender']
    obj.country = request.POST['country']
    obj.state = request.POST['state']
    obj.blood_group = request.POST['blood_group']
    obj.donor_type = request.POST['donor_type']
    obj.save()
    return redirect('/donor')


def find_donor(request):
    donors = Donors.objects.all()

    context = {
        'donors': donors
    }
    return render(request,'donor.html',context)