from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from . import scrape_my_data as sd
from bs4 import BeautifulSoup
import requests
import datetime

# Create your views here.

today = datetime.date.today()

def index(request):
    sd.scrapeNigeria()
    # case_summary = NigeriaTotalCases.objects.all()
    context = {
        'date': today,
        'case_summary': NigeriaTotalCases.objects.all(),
        'cases': NigerianCases.objects.all()
    }
    return render(request,'pandemicHome.html',context)


def globalRecords(request):
    sd.scrapeGlobal()
    context = {
        'date': today,
        'global_summary': GlobalTotalCases.objects.all(),
        'globalRecord': GlobalCases.objects.all()
    }
    return render(request,'global.html',context)


def Faqs(request):
    stated_guides = Faq.objects.all().order_by('-created_at')
    context = {
        'health_guides': stated_guides
    }
    return render(request,'faq.html',context)

def guide(request):
    return render(request,'guides.html')

def highlight(request):
    return render(request,'highlight.html')


def report(request):
    return render(request, 'report.html')


def about(request):
    return render(request,'about.html')