import calendar
from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserChangeForm
from django.middleware.csrf import get_token
from .models import Event, User
from .forms import EventForm, CustomAuthenticationForm, CustomUserCreationForm
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def calendar_view(request):
    now = datetime.now()
    year = now.year
    month = now.month
    
    cal = calendar.Calender()
    
    month_days = cal.monthdayscalendar(year, month)
    
    context = {
        'month_days': month_days,
        'year': year,
        'month': month,
        'month_name': cal.month_name[month],
    }
    
    return render(request, 'calendar.html', context)

# @login_required
# def calendar_view(request):
#     events = Event.objects.filter(owner=request.user)
#     return render(request, 'calendar.html', {'events': events})

# @login_required
# def create_event(request):
#     if request.method == 'POST':
#         form = EventForm(request.POST)
#         if form.is_valid():
#             event = form.save(commit=False)
#             event.owner = request.user
#             event.save()
#             return redirect('calendar')
#     else:
#         form = EventForm()
#     return render(request, 'event_form.html', {'form': form})

# @login_required
# def update_event(request, event_id):
#     event = get_object_or_404(Event, id=event_id)
#     if request.method == 'POST':
#         form = EventForm(request.POST, instance=event)
#         if form.is_valid():
#             form.save()
#             return redirect('calendar')
#     else:
#         form = EventForm(instance=event)
#     return render(request, 'event_form.html', {'form': form})

# @login_required
# def delete_event(request, event_id):
#     event = get_object_or_404(Event, id=event_id)
#     if request.method == 'POST':
#         event.delete()
#         return redirect('calendar')
#     return render(request, 'event_confirm_delete.html', {'event': event})

# @login_required
# def event_details(request, event_id):
#     return HttpResponse(f'Event Details Page - Event ID: {event_id}')

# @login_required
# def event_data(request):
#     events = Event.objects.filter(owner=request.user).values('id', 'title', 'start', 'end')
#     events_list = list(events)
#     return JsonResponse(events_list, safe=False)

@login_required
def chat(request):
    return HttpResponse('Chat Page')

@login_required
def forum(request):
    return HttpResponse('Forum Page')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    print(f"Authenticated User: {request.user}")
    print(f"User PK: {request.user.pk}")
    print(f"CSRF Token: {get_token(request)}")
    
    try:
        user = get_object_or_404(User, pk=request.user.pk)
    except Exception as e:
        print(f"Error retrieving user: {e}")
        return HttpResponse('User not found', status=404)
    
    return render(request, 'profile.html', {'user': user})

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'update_profile.html', {'form': form})

@login_required
def contact(request):
    return render(request, 'contact.html')

def learning_apps(request):
    return HttpResponse('Learning Apps Page')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = CustomAuthenticationForm