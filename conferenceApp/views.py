from django.shortcuts import render
from .models import Conference
from .forms import ConferenceModelForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from userApp.models import Reservation
from categoryApp.models import Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.
def conferenceList(request):
    list = Conference.objects.all()
    return render(request, 'conferences/conference_list.html', {
        'list' : list
    })
    

class ConferenceListView(ListView):
    model = Conference
    template_name = 'conferenceApp/conference_list.html'
    context_object_name='list'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()  
        user_reservations = Reservation.objects.filter(participant=self.request.user).values_list('conference_id', flat=True)
        context['user_reservations'] = user_reservations  # Liste des IDs de conférences réservées par l'utilisateur
        
        return context
    def get_queryset(self):
        queryset= Conference.objects.all().order_by('start_date')
        category_id = self.request.GET.get('category')  
        if category_id:
            queryset = queryset.filter(category_id=category_id)  
        return queryset
    

class ConferenceDetailView(LoginRequiredMixin, DetailView):
    model = Conference
    template_name = 'conferenceApp/conference_detail.html'
    context_object_name = 'conference'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        conference = self.get_object()
        # Récupérer les réservations associées à cette conférence
        context['reservations'] = Reservation.objects.filter(conference=conference)
        return context
    

class ConferenceCreateView(LoginRequiredMixin, CreateView):
    model = Conference
    form_class = ConferenceModelForm
    template_name = 'conferenceApp/conference_form.html'
    #fields = ['title', 'description', 'start_date', 'end_date', 'location', 'price', 'capacity', 'program', 'category']
    success_url = reverse_lazy('conference_list')


class ConferenceUpdateView(LoginRequiredMixin, UpdateView):
    model = Conference
    template_name = 'conferenceApp/conference_form.html'
    fields = ['title', 'description', 'start_date', 'end_date', 'location', 'price', 'capacity', 'program', 'category']
    success_url = reverse_lazy('conference_list')


class ConferenceDeleteView(LoginRequiredMixin, DeleteView):
    model = Conference
    template_name = 'conferences/conference_confirm_delete.html'
    success_url = reverse_lazy('conference_list')