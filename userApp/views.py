from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Participant
from .forms import ParticipantCreationForm  # Crée ce formulaire
from django.contrib.auth.views import LoginView,LogoutView 
from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Conference, Reservation
class UserCreateView(CreateView):
    model = Participant
    form_class = ParticipantCreationForm
    template_name = 'userApp/register.html'
    success_url = reverse_lazy('login')  
class CustomLoginView(LoginView):
    template_name = 'userApp/login.html'
    def get_success_url(self):
        return reverse('conference_list')
    # or LOGIN_REDIRECT_URL = '/conferences/listView'  in the settings.py 
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login') 

@login_required(login_url="login")
def reserve_conference(req,conference_id):
    user=req.user
    conference = get_object_or_404(Conference, id=conference_id)
    if Reservation.objects.filter(participant=user,conference=conference).count() ==0:
        res=Reservation.objects.create(participant=user,conference=conference)
        res.save()
        conference.capacity-=1
        conference.save()
    return redirect('conference_list')