import os
import shutil
import json
import glob
import subprocess
import time
from tracemalloc import Statistic
from turtle import heading
from uuid import uuid1
import PIL    
from django.core import serializers

import datetime
from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from .models import Course, HomeBanner, HomeImages, MasterLabels, Navbar, ProjectCarousel,Statics,Services,Events,Team,Blogs,Clients,Testimonials

def pagelabel(lang):
    
    langqueryset = list(MasterLabels.objects.filter(lang=lang).values('keydata', 'label'))
    dictvalue={}
    for item in langqueryset:
        dictvalue[item['keydata']] = item['label']
    return dictvalue

def home(request):
    lang='en'
    context=pagelabel(lang)

    homeimages=HomeImages.objects.filter(lang=lang).values()
    
    dictvar=dict()
    for img in homeimages:
        dictvar[img['keydata']]=img['pic']
        
    context['courses']=Course.objects.filter(lang=lang).values()
    context['banners']=HomeBanner.objects.filter(lang=lang).values()
    context['projectcarousel']=ProjectCarousel.objects.filter(lang=lang).values()
    context['homeimages']=dictvar
    context['statistic']=Statics.objects.filter(lang=lang).values()
    context['services']=Services.objects.filter(lang=lang).values()
    
    context['events']=Events.objects.filter(lang=lang).values() 
    context['teams']=Team.objects.filter(lang=lang).values() 
    context['blogs']=Blogs.objects.filter(lang=lang).values()  
    context['clients']=Clients.objects.filter(lang=lang).values() 
    context['testimonials']=Testimonials.objects.filter(lang=lang).values() 
    context['navbar']=Navbar.objects.filter(lang=lang).values() 
    context['blogs']=Blogs.objects.filter(lang=lang).values()
    
    
    return render(request, 'pages/index.html', context)
     
def about(request):
    lang='en'
    context=pagelabel(lang)
    return render(request, 'pages/about.html', context)


def blogdetail(request,id):
    lang='en'
    context=pagelabel(lang)
    blogs=Blogs.objects.filter(lang=lang,heading=id).values()
    for i in blogs:
        blog=i
    

    
    context['blog']=blog
    return render(request, 'pages/blogdetail.html', context)

def bloggrid(request):
    lang='en'
    context=pagelabel(lang)
    return render(request, 'pages/bloggrid.html', context)

def bloglist(request):
    lang='en'
    context=pagelabel(lang)
    return render(request, 'pages/bloglist.html', context)

def causesdetail(request):
    lang='en'
    context=pagelabel(lang)
    return render(request, 'pages/causesdetail.html', context)

def causesgrid(request):
    lang='en'
    context=pagelabel(lang)
    return render(request, 'pages/causesgrid.html', context)

def causeslist(request):
    lang='en'
    context=pagelabel(lang)
    return render(request, 'pages/causeslist.html', context)

def contact(request):
    lang='en'
    context=pagelabel(lang)
    return render(request, 'pages/contact.html', context)

def donatenow(request):
    lang='en'
    context=pagelabel(lang)
    return render(request, 'pages/donatenow.html', context)

def eventdetails(request):
    lang='en'
    context=pagelabel(lang)
    return render(request, 'pages/eventdetails.html', context)

def eventgrid(request):
    lang='en'
    context=pagelabel(lang)
    return render(request, 'pages/eventgrid.html', context)

def eventlist(request):
    lang='en'
    context=pagelabel(lang)
    return render(request, 'pages/eventlist.html', context)

def faq(request):
    lang='en'
    context=pagelabel(lang)
    return render(request, 'pages/faq.html', context)

def gallery(request):
    lang='en'
    context=pagelabel(lang)
    return render(request, 'pages/gallery.html', context)

def register(request):
    lang='en'
    context=pagelabel(lang)
    return render(request, 'pages/register.html', context)

def lico(request):
    lang='en'
    context=pagelabel(lang)
    return render(request, 'pages/lico.html', context)

def ikf(request):
    lang='en'
    context=pagelabel(lang)
    return render(request, 'pages/ikf.html', context)
def search(request):
    lang='en'
    context=pagelabel(lang)
    return render(request, 'pages/search.html', context)

def services(request):
    lang='en'
    context=pagelabel(lang)
    return render(request, 'pages/services.html', context)

def tables(request):
    lang='en'
    context=pagelabel(lang)
    return render(request, 'pages/tables.html', context)

def tabs(request):
    lang='en'
    context=pagelabel(lang)
    return render(request, 'pages/tabs.html', context)
def volunteer(request):
    lang='en'
    context=pagelabel(lang)
    return render(request, 'pages/volunteer.html', context)