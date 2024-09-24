from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add_account(request):
    return render(request, 'Add Account Page')

def profile(request):
    return HttpResponse('Profile Page')

def home(request):
    return render(request, 'home.html')

def learning_apps(request):
    return HttpResponse('Learning Apps Page')

def add_event(request):
    return HttpResponse('Add Event Page')

def event_details(request, event_id):
    return HttpResponse(f'Event Details Page - Event ID: {event_id}')

def chat(request):
    return HttpResponse('Chat Page')

def forum(request):
    return HttpResponse('Forum Page')

def calendar(request):
    return HttpResponse('Calendar Page')