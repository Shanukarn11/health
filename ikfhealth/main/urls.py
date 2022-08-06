from django.contrib import admin
from django.urls import path
from main import views
from django.conf.urls.static import static
from django.conf import settings
import re


urlpatterns = [
    path("", views.home, name='home'),
    path("about", views.about, name='about'),
    path("blogdetail/<str:id>", views.blogdetail, name='blogdetail'),
    path("bloggrid", views.bloggrid, name='bloggrid'),
    path("bloglist", views.bloglist, name='bloglist'),
    path("causesdetail", views.causesdetail, name='causesdetail'),
    path("causesgrid", views.causesgrid, name='causesgrid'),
    path("causeslist", views.causeslist, name='causeslist'),
    path("contact", views.contact, name='contact'),
    path("donatenow", views.donatenow, name='donatenow'),
    path("eventdetails", views.eventdetails, name='eventdetails'),
    path("eventgrid", views.eventgrid, name='eventgrid'),
    path("eventlist", views.eventlist, name='eventlist'),
    path("faq", views.faq, name='faq'),
    path("gallery", views.gallery, name='gallery'),
    path("register", views.register, name='register'),
    path("lico", views.lico, name='lico'),
    path("ikf", views.ikf, name='ikf'),
    path("search", views.search, name='search'),
    path("services", views.services, name='services'),
    path("tables", views.tables, name='tables'),
    path("tabs", views.tabs, name='tabs'),
    path("volunteer", views.volunteer, name='volunteer'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)