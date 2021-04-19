from django.shortcuts import render, redirect
from decouple import config
from requests import Request, post,get
from urllib.parse import urlparse
from .authHandling import getuserdata
from django.db.models.signals import request_finished
from django.dispatch import receiver



spotify = getuserdata()

def getauth(request):
    return spotify.getauth(request)

def callback(request):
    return spotify.spotify_callback(request)

def getuserdata(request):
    return spotify.userdata(request)

def no_data(request):
    return render(request, 'nodata.html')

def landingPage(request):
    return render(request, 'landingpage.html')

def on_error(request):
    return render(request, 'onerror.html', context={ 'auth': 'http://127.0.0.1:8000/get-auth-url/'})

@receiver(request_finished, sender=waiting_page)
def generating_stats(request):
    return spotify.generating_stats(request)

def waiting_page(request):
    return spotify.waiting(request)
